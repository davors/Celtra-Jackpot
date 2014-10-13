#-- imports --#
from configuration import *
from fileIO import *
from SampleAnalyzer import *
from evaluation import *
from ConstructCases import *

#-- main program procedure (user code) --#

allCases = constructTestCases()

#test_01_05 = [ allCases[i] for i in [0, 1, 2, 3, 4] ]
#test_06_10 = [ allCases[i] for i in [5, 6, 7, 8, 9] ]
#test_01_10 = [ allCases[i] for i in xrange(10) ]
test_all = [ allCases[i] for i in xrange(len(allCases)) ]

evaluation_batch_cases([allCases[9]], 100)
#evaluation_batch_cases([allCases[1]], 100)

#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_09_04m_30000p_00024r.txt')

##TODO
#Optimize(
#    test_all,
#    GLODEF_OPTIMIZATION_ANNEALING,
#    [],
#    10,
#    DEFAULT_FITNESS_METRIC,
#    [DEFAULT_SELECTION_ALGORITHM, DEFAULT_CHANGEPOINT_ALGORITHM, DEFAULT_RESET_ALGORITHM], 
#    DEFAULT_FUNCTION_APPROXIMATOR
#    )



#### -------- OLD ---------- ###

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
#(case, machines, pulls, reps, data)=loadDataFromFile('case_06_02m_01000p.txt')
#M=[machine(m+1) for m in range(machines)]

#pulls=1000
#for i in range(0,500):
#    data[0][i]=int(random.random()<0.6)
#    data[1][i]=int(random.random()<0.4)

#for i in range(500,1000):
#    data[0][i]=int(random.random()<0.4)
#    data[1][i]=int(random.random()<0.6)

#Y=[]
#X=0
#m=2
#Y2=0
#HP=0
#mt=0
#Mt=0
#for i in range(1,pulls+1):
#    X=X+data[m-2][i-1]
#    (s,A,Y)=checkChange(2.5,X, Y, i, data[m-2][0:i])
#    #(s,A,Y)=checkChange(1.96,X, Y, i, data[m-2][0:i])
#    if(s>0):
#        print 'checkChange triggered at: '+str((s,A,Y,i))
#        break
    #(status, HP, Mt, Y2)=HankeyPankeyTest(80,HP, Mt,data[m-2][i-1], Y2, i)
    #if(status==1):
    #    print 'HankeyPankey triggered at: '+str((HP,i))
    #    break

#print str(case)    