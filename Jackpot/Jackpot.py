import configuration
from changePointDetection import checkChange
from fileIO import *

#for c in range(1,configuration.N_CASES+1):
#    machines=getNumMachines(c)
#    pulls=getNumPulls(c)
#    reps=1
    
#    #if c<=5: 
#    #    reps=20000/pulls
#    #else: 
#    #    reps=20000
#    if configuration.TEST==1:
#        writeDataToFile(c,machines,pulls,reps)

(case, machines, pulls, reps, data)=loadDataFromFile('case_01_02m_00500p.txt')
Y=[]
X=0
m=2
for i in range(1,10):
    X=X+data[m-1][i-1]
    (s,t,Y)=checkChange(X, Y, i, data[m-1][0:i])