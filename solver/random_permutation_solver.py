import sys
import numpy as np
import time
from helper.solution_store_helper import store_solution

SOLVER_NAME = "random_permutation_solver"

def compute_path_length(path,problem):
    return np.sum(np.linalg.norm(problem[path[1:]] - problem[path[:-1]],axis=1))

def solve(problem):
    # initial random path
    opt_path = np.random.permutation(8)
    opt_length = compute_path_length(opt_path,problem)

    # search through a few random permutations
    for itr in range(64):
        path = np.random.permutation(8)
        length = compute_path_length(path,problem)

        if(length < opt_length):
            opt_path = path
            opt_length = length
    
    # return best path found
    return opt_path

def compute():
    # load problem
    filepath = open(sys.argv[1]) 
    problem = np.loadtxt(filepath,delimiter=',')

    # start solver
    start = time.time()
    solution_path = solve(problem)
    end = time.time()

    duration = end-start

    #store solution
    store_solution(SOLVER_NAME,filepath,solution_path,duration)

# start solver
compute()