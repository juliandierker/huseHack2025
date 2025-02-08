import subprocess
import os 

solver_path = "solver/"
problem_path = "problems/"

# load all solvers
all_solver_filenames = os.listdir(solver_path)
all_solver_paths = [os.path.join(solver_path,solver_filename) for solver_filename in all_solver_filenames]

print("all solver filenames:",all_solver_filenames)
print("all solver pathes:",all_solver_paths)

# load all problems
all_problem_filenames = os.listdir(problem_path)
all_problem_paths = [os.path.join(problem_path,problem_filename) for problem_filename in all_problem_filenames]

print("all problem filenames:",all_problem_filenames)
print("all problem file paths",all_problem_paths)

# execute all solvers on all problems
for solver_path in all_solver_paths:
    print("[BENCHMARK] running solver: ",solver_path)
    for idx,problem_path in enumerate(all_problem_paths):
        print("[BENCHMARK] problem",idx+1,"/",len(all_problem_filenames))
        subprocess.run(["python",solver_path,problem_path])