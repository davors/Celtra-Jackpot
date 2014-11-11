#-- user defined cases/bandits --#
#instructions:
#   put each case in its own line
#   the list is structured as follows:
#           number of bandits in case
#                  number of pulls
#                               pull intervals of each bandit (must always start with [0])
#                               probabilities at each interval of each bandit
#

GLODEF_ALLCASES_DEFINES = [

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

        #Celtra testcase 9
        [   4   ,  30000    ,   [   [0, 12000] , [0], [0, 12000], [0] ]   ,
                                [   [0.0, 0.020] , [0], [0.0, 0.023] , [0] ]   ] ,

        #Celtra testcase 10
        [  10   ,  30000   ,    [ [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] , [0,6000,12000,24000] ]   ,
                                [ [0.01, 0.02, 0.01, 0.01] , [0.01, 0.01, 0.02, 0.01] , [0.01, 0.02, 0.01, 0.01]  , [0.01, 0.01, 0.01, 0.02]  , [0.01, 0.01, 0.01, 0.02] , [0.01, 0.01, 0.01, 0.02] , [0.01, 0.02, 0.01, 0.01] , [0.01, 0.02, 0.01, 0.01] , [0.01, 0.01, 0.02, 0.01] , [0.01, 0.01, 0.02, 0.01] ]   ] ,

        #Tom: Celtra-similar testcases (stationary)
        [   2   ,  500     ,    [   [0] ,   [0] ]   ,
                                [ [0.1] , [0.9] ]   ] ,
        [   2   ,  100     ,    [   [0] ,   [0] ]   ,
                                [ [0.1] , [0.9] ]   ] ,
        [   2   ,  500     ,    [   [0] ,   [0] ]   ,
                                [ [0.49] , [0.51] ]   ] ,
        [   2   ,  500     ,    [   [0] ,   [0] ]   ,
                                [ [0.0] , [1.0] ]   ] ,
        [   2   ,  1000     ,    [   [0] ,   [0] ]   ,
                                [ [0.98] , [0.99] ]   ] ,
        [   2   ,  10000   ,    [    [0] ,     [0] ]   ,
                                [ [0.003] , [0.0015] ]   ] ,
        [   3   ,  1000    ,    [   [0] ,    [0] ,    [0] ]   ,
                                [ [0.8] , [0.75] , [0.70] ]   ] ,
        [   3   ,  1000    ,    [   [0] ,    [0] ,    [0] ]   ,
                                [ [0.02] , [0.015] , [0.010] ]   ] ,
        [   3   ,  1000    ,    [   [0] ,    [0] ,    [0] ]   ,
                                [ [0.3] , [0.3] , [0.25] ]   ] ,
        [   4   ,  10000   ,    [    [0] ,    [0] ,     [0],     [0] ]   ,
                                [ [0.92] , [0.92] , [0.925] , [0.92] ]   ] ,
        [   4   ,  10000   ,    [    [0] ,    [0] ,     [0],     [0] ]   ,
                                [ [0.02] , [0.02] , [0.015] , [0.02] ]   ] ,
        [  10   ,  10000   ,    [     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ]   ,
                                [ [0.990] , [0.98] , [0.98] , [0.99] , [0.98] , [1.000] , [0.97] , [0.97] , [0.97] , [0.97] ]   ] ,
        [  10   ,  10000   ,    [     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ,     [0] ]   ,
                                [ [0.010] , [0.009] , [0.009] , [0.060] , [0.061] , [0.110] , [0.112] , [0.110] , [0.110] , [0.111] ]   ] ,

        #Tom: Celtra-similar testcases (non-stationary)
        [   2   ,  1000    ,    [   [   0,   500,  750] , [   0,   500,  750] ]   ,
                                [   [0.55,  0.45, 0.85] , [0.45,  0.55, 0.70] ]   ] ,
        [   2   ,  1000    ,    [   [   0,   500,  750] , [   0,   500,  750] ]   ,
                                [   [1.0,  0.0, 1.0] , [0.0,  1.0, 0.0] ]   ] ,
        [   2   ,  1000    ,    [   [   0,   500,  750] , [   0,   500,  750] ]   ,
                                [   [0.55,  0.85, 0.85] , [0.45,  0.55, 1.00] ]   ] ,
        [   2   ,  1000    ,    [   [   0,   500,  750] , [   0,   500,  750] ]   ,
                                [   [0.55,  0.45, 0.35] , [0.50,  0.45, 0.40] ]   ] ,
        [   2   ,  1000    ,    [   [   0,   250,  500,  750] , [   0,   500,  750] ]   ,
                                [   [0.55,  0.70, 0.45, 0.35] , [0.50,  0.45, 0.40] ]   ] ,
        [   2   ,  15000    ,   [   [0, 4000, 6000] , [0, 4000, 7000] ]   ,
                                [   [0.93, 0.92, 0.93] , [0.915, 0.940, 0.917] ]   ] ,
        [   2   ,  15000    ,   [   [0, 3000, 5000, 7000, 13000] , [0, 4000, 11000] ]   ,
                                [   [0.03, 0.02, 0.03, 0.02, 0.03] , [0.015, 0.040, 0.017] ]   ] ,
        [   3   ,  3000    ,    [   [0, 500, 750, 2500, 2750] , [0, 500, 750, 2500, 2750], [0,1250] ]   ,
                                [   [1.0, 0.0, 1.0, 0.5, 0.7] , [0.8, 0.2, 0.6, 0.6, 0.4] , [0.4, 0.6] ]   ] ,
        [   3   ,  3000    ,    [   [0, 500, 750, 2500, 2750] , [0, 500, 750, 2500, 2750], [0,1250] ]   ,
                                [   [0.0, 0.1, 0.2, 0.3, 0.4] , [0.0, 0.12, 0.24, 0.36, 0.48] , [0.0, 0.3] ]   ] ,
        [   3   ,  3000    ,    [   [0, 500, 750, 2500, 2750] , [0, 500, 750, 2500, 2750], [0,1250] ]   ,
                                [   [0.0, 0.01, 0.02, 0.03, 0.04] , [0.0, 0.012, 0.024, 0.036, 0.048] , [0.0, 0.03] ]   ] ,
        [   4   ,  30000    ,   [   [0, 1000, 2000, 3000, 4000, 5000, 28000] , [0,3000,4000], [0, 1000, 2000, 3000, 4000, 5000, 28000], [0,4000,5000] ]   ,
                                [   [0.0, 0.05, 0.0, 0.05, 0.0, 0.05, 0.1] , [0, 0.05, 0], [0.05, 0.0, 0.05, 0.0, 0.0, 0.049, 0.2] , [0, 0.05,0.0] ]   ] ,
        [   4   ,  30000    ,   [   [0, 1000, 2000, 3000, 4000, 5000, 28000] , [0,3000,4000], [0, 1000, 2000, 3000, 4000, 5000, 28000], [0,4000,5000] ]   ,
                                [   [0.0, 0.05, 0.0, 0.05, 0.0, 0.05, 0.1] , [0, 0.1, 0], [0.05, 0.0, 0.05, 0.0, 0.0, 0.049, 0.2] , [0, 0.1, 0.0] ]   ] ,
        [  10   ,  30000   ,    [ [0,6500,12500,24500] , [0,6500,12500,24500] , [0,6500,12500,24500] , [0,6500,12500,24500] , [0,5000,11000,23000] , [0,5000,11000,23000] , [0,5000,11000,23000] , [0,5000,11000,23000] , [0,4000,10000,22000] , [0,4000,10000,22000] ]   ,
                                [ [0.01, 0.02, 0.03, 0.01] , [0.01, 0.03, 0.02, 0.01] , [0.01, 0.02, 0.01, 0.03]  , [0.03, 0.01, 0.01, 0.02]  , [0.03, 0.01, 0.01, 0.02] , [0.01, 0.03, 0.01, 0.02] , [0.01, 0.02, 0.03, 0.01] , [0.03, 0.02, 0.01, 0.01] , [0.01, 0.03, 0.02, 0.01] , [0.01, 0.01, 0.02, 0.03] ]   ] ,
        [  10   ,  30000   ,    [ [0,3000, 6500,12500, 15000, 24500] , [0,6500,12500,24500] , [0,2000, 6500,12500,15000, 17000, 24500] , [0,6500,12500,24500] , [0,5000,11000,15000, 17000,23000] , [0,5000,11000,23000] , [0, 1000, 2000, 5000,11000,23000] , [0,5000,11000,18000, 20000, 23000] , [0,4000,10000,22000] , [0,4000,10000,22000, 27000] ]   ,
                                [ [0.01, 0.015, 0.02, 0.03, 0.015, 0.01] , [0.01, 0.03, 0.02, 0.01] , [0.01, 0.015, 0.02, 0.01,0.025, 0.02, 0.03]  , [0.01, 0.03, 0.02, 0.01] , [0.03, 0.01, 0.01, 0.015, 0.025, 0.02]  , [0.03, 0.01, 0.01, 0.02] , [0.01, 0.05, 0.04, 0.03, 0.01, 0.02] , [0.01, 0.02, 0.03, 0.02, 0.03, 0.01] , [0.03, 0.02, 0.01, 0.01] , [0.01, 0.01, 0.02, 0.03, 0.05] ]   ] ,



        ##Nejc testcase 1
        #[   2   ,  1000    ,    [   [0] , [0] ]   ,
        #                        [   [0.9] , [0.1] ]  ] ,




             ]

