from webClient import *
def writeDataToFile(case, machines, pulls):
    fileName='case_'+ format(case,'02')+'_'+format(machines,'02')+'_'+format(pulls,'05')
    try:
        f=open(fileName,'w')
        f.write(str(case)+'\t'+str(machines)+'\t'+str(pulls)+'\n')
        for pull in range(1,pulls+1):
            for m in range(1,machines+1):
                f.write(str(getMachineResponse(case, m, pull))+'\t')
            f.write('\n')
        print 'Test case '+str(case)+' written to file '+fileName 
    except:
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
        for pull in range(0,pulls):
            line=f.readline()
            line=line.split()
            for m in range(0,machines):
                data[m][pull]=int(line[m])
    except:
        print 'Error reading file: ' + fileName
        return None
    f.close()
    return (case,machines,pulls,data)