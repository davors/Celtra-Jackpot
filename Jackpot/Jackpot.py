import configuration
from changePointDetection import *
from fileIO import *
from SampleAnalyzer import *
from machine import *
from strategy import *
from BanditGenerator import *

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

testcases = [BanditTestCase() for count in xrange(configuration.N_CASES)]

case=0

testcases[case].numBandits = 2
testcases[case].maxPulls = 1000
testcases[case].bandits = [BanditGenerator() for count in xrange(testcases[case].numBandits)]
testcases[case].bandits[0].intervals = [0,500]
testcases[case].bandits[1].intervals = [0,500]
testcases[case].bandits[0].probabilities = [0.5,0.1]
testcases[case].bandits[1].probabilities = [0.1,0.5]
maxReward = testcases[case].calcMaxReward()

M=[machine(m) for m in range(testcases[case].numBandits)]
total_rejected=0
for i in range(0,testcases[0].maxPulls):
    sM=UCBT(M, i-total_rejected, 1.0)
    sM=UCB1(M, i-total_rejected, 1.0)
    #sM=EGreedy(M,0.1)
    r=testcases[case].pullBandit(sM.id,i)
    sM.update(r)
    rejected=checkChange(100,sM)
    total_rejected=total_rejected+rejected
    if rejected>0:
        print 'Change point at global pull: '+str(i)

totalReward=0
for m in M:
    totalReward=totalReward+m.sum_total
    print 'Machine '+str(m.id)+' Total reward: '+str(m.sum_total)+' Total pulls: '+str(m.pulls_total)+' Average reward: '+str(m.mean)

print 'Total reward: '+str(totalReward)+' maximum possible reward: '+str(maxReward)

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





### TOM ###

#testcases = [BanditTestCase() for count in xrange(configuration.N_CASES)]

#testcases[0].numBandits = 2
#testcases[0].maxPulls = 500
#testcases[0].bandits = [BanditGenerator() for count in xrange(testcases[0].numBandits)]
#testcases[0].bandits[0].intervals = [0,250]
#testcases[0].bandits[1].intervals = [0,250]
#testcases[0].bandits[0].probabilities = [0.1,0.5]
#testcases[0].bandits[1].probabilities = [0.5,0.4]
#maxR = testcases[0].calcMaxReward()

#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_06_02m_01000p_1000r.txt')