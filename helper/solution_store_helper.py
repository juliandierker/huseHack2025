import os 
import time

def get_timestamp():
    return time.strftime("%H%M%S")

def store_solution(solver_name,problem_file_path,solution_path,solution_length,computation_time):
    timestamp = get_timestamp()
    
    file_path = "solutions/solution_" + solver_name + "_" + timestamp + ".csv"

    with open(file_path,"w+") as file:
        file.write(solver_name + ',')
        file.write("./" + problem_file_path + ',')
        file.write(str(computation_time) + ',')
        file.write(str(solution_length) + '\n')
        file.write(",".join(map(str,solution_path)))