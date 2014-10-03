from webClient import *
import sys
from time import sleep
def writeDataToFile(case, machines, pulls, reps):
    fileName='case_'+ format(case,'02')+'_'+format(machines,'02')+'m_'+format(pulls,'05')+'p.txt'
    try:
        f=open(fileName,'w')
        f.write(str(case)+'\t'+str(machines)+'\t'+str(pulls)+'\t'+str(reps)+'\n')
        
        for pull in range(1,pulls+1):
            m=1
            while m<=machines:
                r=getMachineResponse(case, m, pull)
                if r==-1:
                    continue
                else:
                    f.write(str(r)+'\t')
                    m=m+1
            f.write('\n')
        print 'Test case '+str(case)+' written to file '+fileName 
    except:
        print "Unexpected error:" + str(sys.exc_info())
        print 'Error writing to file: ' + fileName
    f.close()

def loadDataFromFile(fileName):
    try:
        f=open(fileName,'r')
        line=f.readline()
        line=line.split()
        case=int(line[0])
        machines=int(line[1])
        pulls=int(line[2])
        reps=int(line[3])
        for pull in range(0,pulls):
            line=f.readline()
            line=line.split()
            for m in range(0,machines):
                data[m][pull]=int(line[m])
    except:
        print 'Error reading file: ' + fileName
        return None
    f.close()
    return (case, machines, pulls, reps, data)