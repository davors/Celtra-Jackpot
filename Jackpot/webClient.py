import urllib2



def getNumMachines(case):
    response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/machines')
    numMachines = response.read()
    if numMachines != 'ERR':
        return int(numMachines)

    return -1


def getNumPulls(case):
    response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/pulls')
    numPulls = response.read()
    if numPulls != 'ERR':
        return int(numPulls)

    return -1
   
   
def getMachineResponse(case, machine, pull):
    response = urllib2.urlopen('http://celtra-jackpot.com/' + str(case) + '/' + str(machine) + '/' + str(pull))
    pullResponse = response.read()
    if pullResponse != 'ERR':
        return int(pullResponse)
    return -1