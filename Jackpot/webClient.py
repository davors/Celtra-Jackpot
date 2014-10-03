import urllib2
import urllib

#get number of machines available in the case
def getNumMachines(case):
    try:
        response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/machines')
        numMachines = response.read()
        if numMachines != 'ERR':
            return int(numMachines)
    except urllib2.URLError as e:
        #print e.reason
        #print '\n'
        return -1
    return -1

#get number of pulls available in the case
def getNumPulls(case):
    try:
        response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/pulls')
        numPulls = response.read()
        if numPulls != 'ERR':
            return int(numPulls)
    except urllib2.URLError as e:
        #print e.reason
        #print '\n'
        return -1
    return -2
   
#pull the machine and get response   
def getMachineResponse(case, machine, pull):
    try:
        response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/' + str(machine) + '/' + str(pull))
        pullResponse = response.read()
        if pullResponse != 'ERR':
            return int(pullResponse)
    except urllib2.URLError as e:
        #print e.reason
        #print '\n'
        return -1
    return -2