import sys
import numpy as np
import time
sys.path.insert(0, './helper')
from solution_store_helper import store_solution

SOLVER_NAME = "random_permutation_solver"

def compute_path_length(path,problem):
    return np.sum(np.linalg.norm(problem[path[1:]] - problem[path[:-1]],axis=1))

def solve(problem):
    # initial random path
    n = len(problem)
    opt_path = np.random.permutation(n)
    opt_length = compute_path_length(opt_path,problem)

    # search through a few random permutations
    for itr in range(64):
        path = np.random.permutation(n)
        length = compute_path_length(path,problem)

        if(length < opt_length):
            opt_path = path
            opt_length = length
    
    # return best path found
    return opt_path,opt_length

def compute():
    # load problem
    filepath = sys.argv[1]
    problem = np.loadtxt(filepath,delimiter=',')

    # start solver
    start = time.time()
    solution_path,solution_length = solve(problem)
    end = time.time()

    duration = end-start

    #store solution
    store_solution(SOLVER_NAME,filepath,solution_path,solution_length,duration)

# start solver
if __name__ == "__main__":
    compute()