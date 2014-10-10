from BanditGenerator import *

def constructTestCases() :

    #-- user defined cases/bandits --#
    #instructions:
    #   put each case in its own line
    #   the list is structured as follows:
    #           number of bandits in case
    #                  number of pulls
    #                               pull intervals of each bandit (must always start with [0])
    #                               probabilities at each interval of each bandit
    #

    all_cases = [

            #Celtra testcase 1
            [   2   ,  500     ,    [   [0] ,   [0] ]   ,
                                    [ [0.4] , [0.6] ]   ] ,

            #Celtra testcase 2
            [   2   ,  10000   ,    [    [0] ,     [0] ]   ,
                                    [ [0.03] , [0.015] ]   ] ,

            #Celtra testcase 3
            [   3   ,  1000    ,    [   [0] ,    [0] ,    [0] ]   ,
                                    [ [0.2] , [0.15] , [0.10] ]   ] ,

            #Celtra testcase 4                        
            [   4   ,  10000   ,    [    [0] ,    [0] ,     [0],     [0] ]   ,
                                    [ [0.02] , [0.02] , [0.025] , [0.02] ]   ] ,

            #Celtra testcase 5
            [  10   ,  10000   ,    [     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ]   ,
                                    [ [0.010] , [0.009] , [0.009] , [0.010] , [0.011] , [0.010] , [0.012] , [0.010] , [0.010] , [0.011] ]   ] ,

            #Celtra testcase 6
            [   2   ,  1000    ,    [   [  0,  500] , [  0,  500] ]   ,
                                    [   [0.6,  0.4] , [0.4,  0.6] ]   ] ,

            #Celtra testcase 7
            [   2   ,  15000    ,   [   [0, 4000, 11000] , [0, 4000, 11000] ]   ,
                                    [   [0.03, 0.02, 0.03] , [0.015, 0.040, 0.017] ]   ] ,

            #Celtra testcase 8
            [   3   ,  3000    ,    [   [0, 1500, 2250] , [0, 1500, 2250], [0] ]   ,
                                    [   [0.2, 0.0, 0.2] , [0.15, 0.3, 0.0] , [0.1] ]   ] ,

            #Celtra testcase 9 --- NEED ADDITIONAL MEASUREMENTS
            [   4   ,  30000    ,   [   [0, 12000] , [0], [0, 12000], [0] ]   ,
                                    [   [0.0, 0.030] , [0], [0.0, 0.035] , [0] ]   ] ,

            #Celtra testcase 10 --- NEED ADDITIONAL MEASUEREMENTS (currently is just noise)
            [  10   ,  30000   ,    [     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ]   ,
                                    [ [0.012] , [0.014] , [0.012] , [0.012] , [0.012] , [0.012] , [0.012] , [0.02] , [0.014] , [0.014] ]   ] ,


                ]


    #-- automatic generation --#

    total_num_cases = len(all_cases)
    cases = [BanditTestCase() for count in xrange(total_num_cases)]
    for c in xrange(total_num_cases) :
        cases[c].numBandits = all_cases[c][0]
        cases[c].maxPulls = all_cases[c][1]
        cases[c].bandits = [BanditGenerator() for count in xrange(cases[c].numBandits)]
        for b in xrange(cases[c].numBandits) :
            cases[c].bandits[b].intervals = all_cases[c][2][b]
            cases[c].bandits[b].probabilities = all_cases[c][3][b]

    return cases