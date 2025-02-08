import numpy as np
import sys
import os
import time
sys.path.insert(0, './helper')
from solution_store_helper import store_solution

SOLVER_NAME = "random_permutation_solver"

def compute_path_length(path,problem):
    return np.sum(np.linalg.norm(problem[path[1:]] - problem[path[:-1]],axis=1))

def solve(problem):
    path = np.arange(len(problem))
    length = compute_path_length(path,problem)
    return path,length

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
compute()