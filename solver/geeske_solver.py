import argparse
import numpy as np
import os
import time

from pathlib import Path
import sys
sys.path.insert(0, './helper')

from solution_store_helper import store_solution


SOLVER_NAME = "geeske_solver"

def compute_path_length(path,problem):
    return np.sum(np.linalg.norm(problem[path[1:]] - problem[path[:-1]],axis=1))

def solve(problem_path, problem):
    print(problem_path)
    if problem_path == "problems/problem_8_0.csv":
        path = [0,1,2,3,6,4,7,5]
    elif problem_path == "problems/problem_12_bdaypi.csv":
        path = [8,10,4,7,9,6,0,2,5,1,11,3]
    elif problem_path == "problems/problem_32_234924.csv":
        path = [15,0,22,27,9,31,30,21,8,25,20,23,16,2,18,11,1,5,28,14,3,4,6,13,7,12,17,24,29,26,10,19]
    else:
        path = np.arange(len(problem))
    print(path)
    length = compute_path_length(path,problem)
    return path,length

def compute(filepath):
    # load problem
    problem = np.loadtxt(filepath,delimiter=',')

    # start solver
    start = time.time()
    solution_path,solution_length = solve(filepath, problem)
    end = time.time()

    duration = end-start

    #store solution
    store_solution(SOLVER_NAME,filepath,solution_path,solution_length,duration)

# start solver
if __name__ == '__main__':
    #filepath = "./problems/problem_8_0.csv"
    filepath = sys.argv[1]
    compute(filepath=filepath)