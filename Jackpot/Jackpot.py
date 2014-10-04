import configuration
from fileIO import *

for c in range(1,configuration.N_CASES+1):
    machines=getNumMachines(c)
    pulls=getNumPulls(c)
    reps=1
    
    #if c<=5: 
    #    reps=20000/pulls
    #else: 
    #    reps=20000
    if configuration.TEST==1:
        writeDataToFile(c,machines,pulls,reps)
    