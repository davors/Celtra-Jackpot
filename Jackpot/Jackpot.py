import configuration
from fileIO import *

for c in range(1,configuration.N_CASES+1):
    machines=getNumMachines(c)
    pulls=getNumPulls(c)
    if configuration.TEST==1:
        writeDataToFile(c,machines,pulls)
