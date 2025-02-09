import csv
import os
import pandas as pd
import streamlit as st


def read_solution(solution_path):
    with open(solution_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        solution = []
        for row in reader:
            solution.append(row)
    solvername = solution[0][0]
    problempath = solution[0][1]
    time = solution[0][2]
    pathlength = solution[0][3]
    solutionorder = solution[1]
    return solvername, problempath, time, pathlength, solutionorder

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the HuseHack2025! 👋")

st.sidebar.success("Select a page above.")

solution_dirpath = "./solutions"
solutions_list = []

for solution_filename in os.listdir(solution_dirpath):
    if solution_filename.endswith(".csv"):
        solution_path = os.path.join(solution_dirpath, solution_filename)
        solver_name, problem_path, time, path_length, solution_order = read_solution(solution_path)
        solutions_list.append([solver_name, problem_path, time, path_length])
solutions = pd.DataFrame(solutions_list, columns=["solver_name", "problem_path", "time", "path_length"])

best_solutions_list = []
for problem_path in solutions["problem_path"].unique():
    best_solution = pd.DataFrame()
    problem_df = solutions[solutions["problem_path"] == problem_path]
    best_solution = problem_df[problem_df["path_length"] == problem_df["path_length"].min()]
    best_path_length = best_solution["path_length"].values[0]
    best_solver = best_solution["solver_name"].values[0]
    best_solutions_list.append([problem_path, best_solver, best_path_length])
best_solutions = pd.DataFrame(best_solutions_list, columns=["problem_path", "solver_name", "path_length"])

high_score = pd.DataFrame(best_solutions["solver_name"].value_counts())
high_score.insert(loc=1, column="ranking", value=range(len(high_score)))


st.header("High Score")
st.write(high_score)
st.header("Best Solutions")
st.write(best_solutions)