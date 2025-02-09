import numpy as np
import os
import pandas as pd
import streamlit as st

from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from visualization.high_score import read_solution

st.title("Compare Solvers")

solution_dirpath = "./solutions"
solutions_list = []

for solution_filename in os.listdir(solution_dirpath):
    if solution_filename.endswith(".csv"):
        solution_path = os.path.join(solution_dirpath, solution_filename)
        solver_name, problem_path, time, path_length, solution_order = read_solution(solution_path)
        solutions_list.append([solution_filename, solver_name, problem_path, time, path_length])
solutions = pd.DataFrame(solutions_list, columns=["filename", "solver_name", "problem_path", "time", "path_length"])


st.write(solutions)