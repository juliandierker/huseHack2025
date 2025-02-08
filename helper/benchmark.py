import subprocess
import os 

all_solver_filenames = os.listdir("solver")

for filename in all_solver_filenames:
    print("solver: ",filename)


#subprocess.run(["python","solver/example_solver.py","problems/problem_8_0.csv"])