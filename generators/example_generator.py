#%%

import numpy as np
import time

# generate 32 random 2d coordinates
n = 32
coordinates = np.random.random((n,2))

# define problem path with problem size and a timestamp
timestamp = time.strftime("%H%M%S")
problem_path = "problems/problem_"+str(n)+"_"+timestamp+".csv"

# save problem as csv
np.savetxt(problem_path,coordinates,delimiter=',',fmt='%1.5f')

#%%