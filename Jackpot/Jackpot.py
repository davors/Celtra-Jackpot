import configuration
from fileIO import *
from SampleAnalyzer import *


SampleAnalyzer('case_06_02m_01000p_1000r.txt')


#for c in range(3,configuration.N_CASES+1):

    #machines=getNumMachines(c)
    #pulls=getNumPulls(c)
    #reps=1000
    
    ##if c<=5: 
    ##    reps=20000/pulls
    ##else: 
    ##    reps=20000
    #if configuration.TEST==1:
    #    writeDataToFile(c,machines,pulls,reps)
    