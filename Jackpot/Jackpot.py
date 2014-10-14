#-- imports --#
from Config import *
from fileIO import *
from SampleAnalyzer import *
from Jackpot_init import *
from MABsolver import *
from Evaluator import *
from Optimization import *
from unitTests import *

#-- main program procedure (user code) --#

allCases = constructTestCases(GLODEF_ALLCASES_DEFINES)

#Celtra's test batches
testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )
testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )
testBatch_01_10 = BanditTestBatch( allCases, xrange(10) )
testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) )
testBatch_tmp = BanditTestBatch( allCases, [10] )

#unitTest_Optimizer(allCases)

testSolver = MABsolver()
evaluateBatch(testSolver, testBatch_01_10, 100, 0)


#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_09_04m_30000p_00024r.txt')






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
 
# 0 'random'
# 1 'epsilonGreedy
# 2 'softMax'
# 3 'UCB1'
# 4 'UCBtuned'


#def findBestParams(test_cases, repeats, selection_algorithm = 0, param_range = [0], criterion = 0):
#    best_param=0
#    max_score=0
#    for p in param_range:
#        (average_metrics, metrics)=evaluation_batch_cases(test_cases, repeats, selection_algorithm,[p])
#        if average_metrics[criterion]>max_score:
#            max_score=average_metrics[criterion]
#            best_param=p
#    return (best_param)


#allCases = constructTestCases()

#test_01_05 = [ allCases[i] for i in [0, 1, 2, 3, 4] ]
##test_06_10 = [ allCases[i] for i in [5, 6, 7, 8, 9] ]
##test_01_10 = [ allCases[i] for i in xrange(10) ]
##test_all = [ allCases[i] for i in xrange(len(allCases)) ]

#params=list(frange(0,2,0.2))
#best=findBestParams(test_01_05,50,3,params,0)
#print 'Best param value: '+str(best)
#raw_input("Press Enter to continue...")

#evaluation_batch_cases(test_all, 100)
#evaluation_batch_cases([allCases[1]], 100)

#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_09_04m_30000p_00024r.txt')





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