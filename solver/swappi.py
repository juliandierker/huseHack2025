import sys
import numpy as np
import time
sys.path.insert(0, './helper')
from solution_store_helper import store_solution
import numba

SOLVER_NAME = "swappi"

@numba.njit
def try_reduction(path,distances,opt_path_length):
    n = len(path)
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue

            l = opt_path_length

            # temp reduce path length by connecting edges to swap pair
            l -= 0 if i == 0 else distances[path[i-1],path[i]]
            l -= 0 if i == n-1 else distances[path[i],path[i+1]]
            l -= 0 if j == 0 else distances[path[j-1],path[j]]
            l -= 0 if j == n-1 else distances[path[j],path[j+1]]

            # swap pair in path
            t = path[i]
            path[i] = path[j]
            path[j] = t

            # increase length by swapped connections
            l += 0 if i == 0 else distances[path[i-1],path[i]]
            l += 0 if i == n-1 else distances[path[i],path[i+1]]
            l += 0 if j == 0 else distances[path[j-1],path[j]]
            l += 0 if j == n-1 else distances[path[j],path[j+1]]

            if(l < opt_path_length):
                opt_path_length = l
                return True,opt_path_length
            else:
                t = path[i]
                path[i] = path[j]
                path[j] = t
    return False,opt_path_length

def solve(problem):
    distances  = np.linalg.norm(problem[:,np.newaxis] - problem[np.newaxis,...],axis=2)
    n = len(problem)

    path = np.arange(n)
    opt_path_length = sum([np.linalg.norm(problem[i]-problem[i+1]) for i in range(n-1)])
    
    success = True
    while(success):
        success,new_length = try_reduction(path,distances,opt_path_length)
        if(success):
            opt_path_length = new_length
    return path,opt_path_length

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