import urllib2
import urllib


def getNumMachines(case):
    try:
        response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/machines')
        numMachines = response.read()
        if numMachines != 'ERR':
            return int(numMachines)
    except urllib2.URLError as e:
        print e.reason
        return -1
    return -1


def getNumPulls(case):
    try:
        response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/pulls')
        numPulls = response.read()
        if numPulls != 'ERR':
            return int(numPulls)
    except urllib2.URLError as e:
        print e.reason
        return -1
    return -2
   
   
def getMachineResponse(case, machine, pull):
    try:
        response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/' + str(machine) + '/' + str(pull))
        pullResponse = response.read()
        if pullResponse != 'ERR':
            return int(pullResponse)
    except urllib2.URLError as e:
        print e.reason
        return -1
    return -2