import sys
import numpy as np
sys.path.insert(0, './helper')
from solution_store_helper import store_solution
from scipy.cluster.vq import kmeans, vq

import time

SOLVER_NAME = "nearest_neighbour"
CLUSTER_NUMBER = 3

def compute_path_length(path,problem):
    return np.sum(np.linalg.norm(problem[path[1:]] - problem[path[:-1]],axis=1))

def distance_from_origin(node):
    return np.linalg.norm(node)    

def sort_cluster(problemCluster):
    return sorted(range(len(problemCluster)), key=lambda i: distance_from_origin(problemCluster[i]))

def get_cluster_indizes(problem):
    clusterable_problem = np.array(problem, dtype=float)
    centroids, _ = kmeans(clusterable_problem, 2)
    cluster_labels, _ = vq(clusterable_problem, centroids)
    return cluster_labels


def solve(problem):

    return problem, problem


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