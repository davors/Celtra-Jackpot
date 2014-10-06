##
## Reads output from repeated samples and produces a single output file for each case
##

from fileIO import *

def SampleAnalyzer(fileName):
    (case,machines,pulls,repeats,data) = loadDataFromFile(fileName)

    avg_data = [[0.0 for col in range(pulls)] for row in range (machines)]
    for im in range(machines):
        for ip in range(pulls):
            for ir in range(repeats):
                avg_data[im][ip] = avg_data[im][ip] + data[im][ip + pulls*ir]
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
                f.write('%.3f' % (avg_data[m-1][pull-1])+'\t')
            f.write('\n')
        print 'Analyzed test case '+str(case)+' written to file '+fileName 
    except:
        print "Unexpected error:" + str(sys.exc_info())
        print 'Error writing to file: ' + fileName
    f.close()
    print 'File '+fileName+' succesfully averaged'