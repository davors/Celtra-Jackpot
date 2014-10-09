import configuration
from changePointDetection import *
from fileIO import *
from SampleAnalyzer import *
from machine import *
from strategy import *
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
(case, machines, pulls, reps, data)=loadDataFromFile('case_06_02m_01000p.txt')
M=[machine(m+1,pulls) for m in range(machines)]

for i in range(0,500):
    data[0][i]=random.random()<0.4
    data[1][i]=random.random()<0.3

for i in range(500,1000):
    data[0][i]=random.random()<0.3
    data[1][i]=random.random()<0.4

for i in range(1,pulls+1):
    sM=EGreedy(M,0.1)
    r=data[sM.id-1][sM.totalN]
    sM.update(r)
    sM=checkChange(2.5,sM,data)

totalReward=0
for m in M:
    totalReward=totalReward+m.totalReward
    print 'Machine '+str(m.id)+' Total reward: '+str(m.totalReward)+' Total pulls: '+str(m.totalN)+' Average reward: '+str(m.mR)

print 'Total reward: '+str(totalReward)

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


#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_06_02m_01000p_1000r.txt')