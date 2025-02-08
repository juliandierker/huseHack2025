import subprocess
import os 

problem_path = "problems/"
solver_path = "solver/"

all_solver_filenames = os.listdir(solver_path)
all_problem_filenames = os.listdir(problem_path)

# load all problems
all_problems = [os.path.join(problem_path,problem_filepath) for problem_filepath in os.listdir(all_problem_filenames)]

# execute all solvers on all problems
for solver_filename in all_solver_filenames:
    print("[BENCHMARK] running solver: ",solver_filename)
    solver_path = os.path.join(solver_path,solver_filename)
    for idx,problem_filename in enumerate(all_problem_filenames):
        print("[BENCHMARK] problem",idx+1,"/",len(all_problem_filenames))
        problem_path = os.path.join(problem_path,problem_filename)
        subprocess.run(["python",solver_path,problem_path])