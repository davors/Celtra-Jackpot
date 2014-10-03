from webClient import *
import sys
from time import sleep


#   File format used for storing test cases
#   In header: <case> <machines> <pulls> <repeats>
#   In body: <m1p1> <m2p1>  ... <mnp1>
#            <m1p2  <m2p2>  ... <mnp2> 
#            ...
#            <m1pm> <m2pm>  ... <mnpm>   
#            <m1p1> <m2p1>  ... <mnpm>
#            ...
#

#Fetch data from Celtra server and store it to file
def writeDataToFile(case, machines, pulls, reps):
    #generate filename
    fileName='case_'+ format(case,'02')+'_'+format(machines,'02')+'m_'+format(pulls,'05')+'p.txt'
    try:
        f=open(fileName,'w')
        #write header
        f.write(str(case)+'\t'+str(machines)+'\t'+str(pulls)+'\t'+str(reps)+'\n')
        for rep in range (1,reps+1):
            for pull in range(1,pulls+1):
                m=1
                while m<=machines:
                    #fetch data from server
                    r=getMachineResponse(case, m, pull)
                    if r==-1:
                        #try again if response invalil or timeout occurs
                        continue
                    else:
                        f.write(str(r)+'\t')
                        m=m+1
                f.write('\n')
                #progress bar
                p=(pull*(m-1)*rep*100)/(reps*pulls*machines)
                print 'Fetching test case '+str(case)+' [%d %%]\r'%p,
        print '\nTest case '+str(case)+' written to file '+fileName+'\n' 
    except:
        print "Unexpected error:" + str(sys.exc_info())
        print 'Error writing to file: ' + fileName
    f.close()

#Load data from file into list
def loadDataFromFile(fileName):
    try:
        f=open(fileName,'r')
        #read header
        line=f.readline()
        line=line.split()
        case=int(line[0])
        machines=int(line[1])
        pulls=int(line[2])
        reps=int(line[3])

        #read line by line
        for rep in range (1,reps+1):
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