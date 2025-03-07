import altair as alt
import pandas as pd
import os
import streamlit as st

from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from visualization.high_score import read_solution

st.title("Display Solutions")

problem_dirpath = "./problems"
solution_dirpath = "./solutions"
solution_filenames = [filename for filename in os.listdir(solution_dirpath) if filename.endswith(".csv")]

st.sidebar.title("Navigation")
solution_filename = st.sidebar.selectbox("Select solution for display", solution_filenames)
display_solution_bool = st.sidebar.checkbox("Display Solution", value=True)

solution_path = os.path.join(solution_dirpath, solution_filename)
solver_name, problem_path, time, path_length, solution_order= read_solution(solution_path)

problem = pd.read_csv(problem_path, header=None)
problem.columns = ["x", "y"]
problem["x"] = problem["x"].astype(float)
problem["y"] = problem["y"].astype(float)
problem = problem.iloc[solution_order]
problem.reset_index(inplace=True)
problem.rename({"index":"solution_order"}, axis=1, inplace=True)
problem.reset_index(inplace=True)

st.write(problem)



chart = alt.Chart(problem).mark_point().encode(x="x", y="y", size="solution_order").interactive()
path = alt.Chart(problem).mark_line(point=True).encode(x='x', y='y', order='index')
if display_solution_bool:
    chart = chart + path

st.write("Solver:", solver_name)
st.write("Problem:", os.path.basename(problem_path))
st.write("Time:", time)
st.write("Pathlength:", path_length)
st.altair_chart(chart, use_container_width=True)
st.write(problem)




