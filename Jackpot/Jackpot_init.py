from BanditGenerator import *

def constructTestCases(all_cases, suppress_output = 0) :

    #user select which cases to generate
    generate_cases = [ all_cases[i] for i in xrange(len(all_cases)) ]   # all cases
    #generate_cases = [ all_cases[i] for i in (0,1,2) ]                  # example for an arbitrary set of cases

    #-- automatic generation --#

    total_num_cases = len(generate_cases)
    
    if(not suppress_output) :
        print ('constructTestCases(): generating %d specified cases ... ' % total_num_cases),

    cases = [BanditTestCase() for count in xrange(total_num_cases)]
    for c in xrange(total_num_cases) :
        cases[c].ID = c
        cases[c].numBandits = generate_cases[c][0]
        cases[c].maxPulls = generate_cases[c][1]
        cases[c].bandits = [BanditGenerator() for count in xrange(cases[c].numBandits)]
        for b in xrange(cases[c].numBandits) :
            cases[c].bandits[b].intervals = generate_cases[c][2][b]
            cases[c].bandits[b].probabilities = generate_cases[c][3][b]
        cases[c].calcMaxReward()
        cases[c].calcRandomReward()

    if(not suppress_output) :
        print 'DONE'

    return cases