##
## Reads output from repeated samples and produces a single output file for each case
##

from fileIO import *

def SampleAnalyzer(fileName):
    (case,machines,pulls,repeats,data) = loadDataFromFile(fileName)

    avg_data = [[0 for col in range(pulls)] for row in range (machines)]
    for im in range(machines):
        for ip in range(pulls):
            for ir in range(repeats):
                avg_data[im][ip] += data[im][ip * (ir-1)]
        for ip in range(pulls):
            avg_data[im][ip] /= repeats

    writeAnalyzedDataToFile(case, machines, pulls, repeats, avg_data)

def writeAnalyzedDataToFile(case, machines, pulls, repeats, avg_data):
    fileName='averaged__case_'+ format(case,'02')+'_'+format(machines,'02')+'m_'+format(pulls,'05')+'p_'+format(repeats,'05')+'r.txt'
    try:
        f=open(fileName,'w')
        f.write(str(case)+'\t'+str(machines)+'\t'+str(pulls)+'\t'+str(repeats)+'\n')
        for pull in range(1,pulls+1):
            for m in range(1,machines+1):
                f.write(str(avg_data[m][pull])+'\t')
            f.write('\n')
        print 'Analyzed test case '+str(case)+' written to file '+fileName 
    except:
        print 'Error writing to file: ' + fileName
    f.close()  