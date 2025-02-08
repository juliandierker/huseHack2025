import sys
import os

def solve():
    file_name = sys.argv[1]
    file_path = file_path = os.path.join("problems", file_name)

    file = open(file_path) # this is the filename of the problem csv
    
    # process the problem blabla
    raw = file.read()
    file.close()
    lines = raw.split('\n')
    number_of_nodes = len(lines)

    # write a csv solution file 
    
    """
    solvimcsolveface # solver name
    problem_8_0 # problem name
    0,1,2,3,4,5,6,7 # solution (ordered indices)
    """


if __name__ == "__main__":
    solve()