import os 
import time

def get_timestamp():
    return time.strftime("%H%M%S")

def store_solution(solver_name,problem_name,solution_path,computation_time):
    timestamp = get_timestamp()
    
    file_path = "solutions/solution_" + solver_name + "_" + timestamp + ".csv"

    with open(file_path,"w+") as file:
        file.write(solver_name + '\n')
        file.write(problem_name + '\n')
        file.write(str(computation_time) + '\n')
        file.write(",".join(map(str,solution_path)))