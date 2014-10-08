import configuration
from changePointDetection import *
from fileIO import *
from SampleAnalyzer import *
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
Y=[]
X=0
m=2
Y2=0
HP=0
mt=0
Mt=0
for i in range(1,pulls+1):
    X=X+data[m-2][i-1]
    (s,A,Y)=checkChange(2.5,X, Y, i, data[m-2][0:i])
    #(s,A,Y)=checkChange(1.96,X, Y, i, data[m-2][0:i])
    if(s>0):
        print 'checkChange triggered at: '+str((s,A,Y,i))
        break
    #(status, HP, Mt, Y2)=HankeyPankeyTest(80,HP, Mt,data[m-2][i-1], Y2, i)
    #if(status==1):
    #    print 'HankeyPankey triggered at: '+str((HP,i))
    #    break

#print str(case)    


#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_06_02m_01000p_1000r.txt')