import sys
import numpy as np
sys.path.insert(0, './helper')
from solution_store_helper import store_solution

import time

SOLVER_NAME = "nearest_neighbour"


def compute_path_length(path,problem):
    return np.sum(np.linalg.norm(problem[path[1:]] - problem[path[:-1]],axis=1))

def distance_from_origin(node):
    return np.linalg.norm(node)    



def solve(problem):
    opt_path = sorted(range(len(problem)), key=lambda i: distance_from_origin(problem[i]))
    opt_length = compute_path_length(opt_path, problem)
    return opt_path, opt_length


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