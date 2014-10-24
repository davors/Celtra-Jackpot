#-- imports --#
from Jackpot_init import *
from Config_testCases import *
from BanditGenerator import *
from fileIO import *
from SampleAnalyzer import *
from MABsolver import *
from Evaluator import *
from Optimization import *
from unitTests import *
import cProfile
import pstats
from experiments import *

###--- main program procedure (user code) ---###

##-- all benchmark scenarios (cases)

allCases = constructTestCases(GLODEF_ALLCASES_DEFINES)

##-- test batches

testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
testBatch_01_10 = BanditTestBatch( allCases, xrange(10) )       #Celtra

testBatch_tmp = BanditTestBatch( allCases, [1,10] )
testBatch_tmp2 = BanditTestBatch( allCases, [2,5] )
testBatch_tmp3 = BanditTestBatch( allCases, [6] )

testBatch_debug = BanditTestBatch( allCases, [5])


##-- experiments (for ICANNGA)

test_2014_10_24_addedEvalCases(allCases)
#test_2014_10_23_linear_3inp_exploration(allCases)
#test_2014_10_20_changePoint_DavorTom2par(allCases)
#test_2014_10_18_noChangePoint(allCases)
#test_2014_10_20_HankeyPankey_treshold(allCases)


##-- unit tests

#unitTest_OptExhaustive(allCases)
#unitTest_OptSimulatedAnnealing(allCases)
#unitTest_Nejc_POKER(allCases)
#unitTest_Nejc_UCBT(allCases)
#unitTest_Nejc_SOFTMAX(allCases)

##-- policy configuration

solv_initial_param_values = None     #if None: default will be used
solv_selection_policy = GLODEF_SELECTION_UCBTUNED
solv_change_point_detector = DEFAULT_CHANGEPOINT_DETECTOR
solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)
#solver = MABsolver()



##-- evaluation

eval_solver = solver
eval_batch_cases = testBatch_debug
eval_suppress_output = 0
eval_num_repeats = 1
eval_oracle_probablity = 0

#evaluateBatch(eval_solver, eval_batch_cases, eval_num_repeats, eval_suppress_output, eval_oracle_probablity)



##-- optimization configuration

#opti_solver = solver
#opti_evaluations_per_sample = 5
#opti_config = DEFAULT_OPTIMIZATION_CONFIG       #configuration for the optimization algorithm: arbitrary list of additional parameters
#opti_fitness_metric = DEFAULT_FITNESS_METRIC
#opti_algorithm = DEFAULT_OPTIMIZATION_ALGORITHM
#opti_selective_optimization = None              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized

#optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)

#opti_learn_cases = testBatch_tmp
#opti_eval_cases = testBatch_tmp2
#opti_completeRepeats = 1
#opti_suppress_output = 0
#opti_oracle_probablity = 1

#optimizer.Optimize(opti_learn_cases, opti_config, opti_completeRepeats, opti_suppress_output, opti_oracle_probablity)

#opti_eval_repeats = 10

#optimizer.OptimizeEvaluate(opti_learn_cases, opti_eval_cases, opti_eval_repeats, opti_config, opti_completeRepeats, eval_suppress_output, opti_oracle_probablity)



##-- example of profiling the computation times

#cProfile.run('evaluateBatch(eval_solver, eval_batch_cases, eval_num_repeats, eval_suppress_output, eval_oracle_probablity)', 'myFunction.profile')
#stats = pstats.Stats('myFunction.profile')
#stats.strip_dirs().sort_stats('time').print_stats()



##-- analizer of samples gathered from URL

#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_09_04m_30000p_00024r.txt')






#### -------- OLD ---------- ###

#for c in range(1,configuration.N_CASES+1):
#    machines=getNumMachines(c)
#    pulls=getNumPulls(c)
#    reps=1
#    #if c<=5:
#    #    reps=20000/pulls
#    #else:
#    #    reps=20000
#    if configuration.TEST==1:
#        writeDataToFile(c,machines,pulls,reps)
#(case, machines, pulls, reps, data)=loadDataFromFile('case_06_02m_01000p.txt')
#M=[machine(m+1) for m in range(machines)]

#pulls=1000
#for i in range(0,500):
#    data[0][i]=int(random.random()<0.6)
#    data[1][i]=int(random.random()<0.4)

#for i in range(500,1000):
#    data[0][i]=int(random.random()<0.4)
#    data[1][i]=int(random.random()<0.6)

# 0 'random'
# 1 'epsilonGreedy
# 2 'softMax'
# 3 'UCB1'
# 4 'UCBtuned'


#def findBestParams(test_cases, repeats, selection_algorithm = 0, param_range = [0], criterion = 0):
#    best_param=0
#    max_score=0
#    for p in param_range:
#        (average_metrics, metrics)=evaluation_batch_cases(test_cases, repeats, selection_algorithm,[p])
#        if average_metrics[criterion]>max_score:
#            max_score=average_metrics[criterion]
#            best_param=p
#    return (best_param)


#allCases = constructTestCases()

#test_01_05 = [ allCases[i] for i in [0, 1, 2, 3, 4] ]
##test_06_10 = [ allCases[i] for i in [5, 6, 7, 8, 9] ]
##test_01_10 = [ allCases[i] for i in xrange(10) ]
##test_all = [ allCases[i] for i in xrange(len(allCases)) ]

#params=list(frange(0,2,0.2))
#best=findBestParams(test_01_05,50,3,params,0)
#print 'Best param value: '+str(best)
#raw_input("Press Enter to continue...")

#evaluation_batch_cases(allCases[5], 1)
#evaluation_batch_cases([allCases[1]], 100)
#evaluation_bactch_cases([allCases[5]],1)

#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_09_04m_30000p_00024r.txt')





#Y=[]
#X=0
#m=2
#Y2=0
#HP=0
#mt=0
#Mt=0
#for i in range(1,pulls+1):
#    X=X+data[m-2][i-1]
#    (s,A,Y)=checkChange(2.5,X, Y, i, data[m-2][0:i])
#    #(s,A,Y)=checkChange(1.96,X, Y, i, data[m-2][0:i])
#    if(s>0):
#        print 'checkChange triggered at: '+str((s,A,Y,i))
#        break
    #(status, HP, Mt, Y2)=HankeyPankeyTest(80,HP, Mt,data[m-2][i-1], Y2, i)
    #if(status==1):
    #    print 'HankeyPankey triggered at: '+str((HP,i))
    #    break

#print str(case)