import altair as alt
import pandas as pd
import os
import streamlit as st

st.title("Display Problems")

problem_dirpath = "./problems"
problem_filenames = os.listdir(problem_dirpath)

st.sidebar.title("Navigation")
problem_filename = st.sidebar.selectbox("Select problem for display", problem_filenames)

problem_path = os.path.join(problem_dirpath, problem_filename)
problem = pd.read_csv(problem_path, header=None)
problem.columns = ["x", "y"]
chart = alt.Chart(problem).mark_point().encode(x="x", y="y").interactive()

st.write(f"Problem with {len(problem)} points")
st.altair_chart(chart, use_container_width=True)
st.write(problem)




