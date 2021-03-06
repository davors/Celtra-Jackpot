from Config import *
from fileIO import *
from SampleAnalyzer import *
from Jackpot_init import *
from MABsolver import *
from Evaluator import *
from Optimization import *
from unitTests import *




def unitTest_OptExhaustive(allCases) :

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra

    solv_initial_param_values = None     #if None: default will be used
    solv_selection_policy = GLODEF_SELECTION_UCBTUNED
    solv_change_point_detector = GLODEF_CHANGEPOINT_DAVORTOM
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)

    opti_solver = solver
    opti_evaluations_per_sample = 1
    opti_config = [ [0.4, 0.02, 21] , [0.1, 0.1, 30] ]       #configuration for the optimization algorithm: arbitrary list of additional parameters
    opti_fitness_metric = DEFAULT_FITNESS_METRIC
    opti_algorithm = GLODEF_OPTIMIZATION_EXHAUSTIVE
    opti_selective_optimization = [0, 1]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized

    optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)

    opti_learn_cases = testBatch_Complete
    opti_completeRepeats = 1
    opti_suppress_output = 0
    opti_oracle_probablity = 1

    optimizer.Optimize(opti_learn_cases, opti_config, opti_completeRepeats, opti_suppress_output, opti_oracle_probablity)

def unitTest_OptSimulatedAnnealing(allCases) :

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra

    testBatch_05 = BanditTestBatch( allCases, [5] ) # 5

    solv_initial_param_values = None     #if None: default will be used
    solv_selection_policy = GLODEF_SELECTION_UCBTUNED
    solv_change_point_detector = GLODEF_CHANGEPOINT_DAVORTOM
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)

    opti_solver = solver
    opti_evaluations_per_sample = 10
    opti_config = [     #configuration for the optimization algorithm: arbitrary list of additional parameters
    [0.0, 0.1],         # lower bounds for all parameters
    [2.0, 5.0],         # upper bounds for all parameters
    [],          # grid step (if you want discrete search); leave empty for continuous search
    10,                 # number of cycles (epochs) of SA
    20,                 # number of iterations per each cycle
    0.2,                # probability of accepting worse solution at the start
    0.001,              # probability of accepting worse solution at the end
    0.50,                # neighbourhood radius at the start (ratio of interval)
    0.01                 # neighbourhood radius at the end (ratio of interval)
    ]

    opti_fitness_metric = DEFAULT_FITNESS_METRIC
    opti_algorithm = GLODEF_OPTIMIZATION_ANNEALING
    opti_selective_optimization = [0, 1]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized

    optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)

    opti_learn_cases = testBatch_05
    opti_completeRepeats = 5
    opti_suppress_output = 0
    opti_oracle_probablity = 0

    optimizer.Optimize(opti_learn_cases, opti_config, opti_completeRepeats, opti_suppress_output, opti_oracle_probablity)

def unitTest_Optimizer(allCases) :
    testBatch_tmp = BanditTestBatch( allCases, [10] )
    testSolver = MABsolver([1.0, 2.5, 0.2, 5], GLODEF_SELECTION_UCBTUNED, GLODEF_CHANGEPOINT_NONE , GLODEF_RESET_ALGORITHM_RESET_ALL_TO_ZERO, GLODEF_PARAM_FUNCTION_DIRECT)
    optimizer = Optimizer(testSolver, 50, [], GLODEF_FITNESS_OPTIMALITY, GLODEF_OPTIMIZATION_ANNEALING, [0])
    optimizer.Optimize(testBatch_tmp, [0.0])
    optimizer.OptimizeEvaluate()

def unitTest_resetAlgorithm_onEvalProb(allCases) :
    blabla




def unitTest_Tom(allCases) :

    testSolver = MABsolver()
    evaluateBatch(testSolver, testBatch_tmp, 100, 0, 1)




def unitTest_allObjects_andParameters():



    ##-- all benchmark scenarios (cases)

    allCases = constructTestCases(GLODEF_ALLCASES_DEFINES)



    ##-- test batches

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, xrange(10) )       #Celtra
    testBatch_tmp = BanditTestBatch( allCases, [1,10] )



    ##-- multi-armed bandit (MAB) solver configuration

    solv_initial_param_values = None     #if None: default will be used
    solv_selection_policy = DEFAULT_SELECTION_POLICY
    solv_change_point_detector = DEFAULT_CHANGEPOINT_DETECTOR
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)
    #solver = MABsolver()



    ##-- evaluation configuration

    eval_solver = solver
    eval_batch_cases = testBatch_01_10
    eval_suppress_output = 0
    eval_num_repeats = 1
    eval_oracle_probablity = 1

    evaluateBatch(eval_solver, eval_batch_cases, eval_num_repeats, eval_suppress_output, eval_oracle_probablity)




    ##-- optimization configuration

    opti_solver = solver
    opti_evaluations_per_sample = 50
    opti_config = DEFAULT_OPTIMIZATION_CONFIG       #configuration for the optimization algorithm: arbitrary list of additional parameters
    opti_fitness_metric = DEFAULT_FITNESS_METRIC
    opti_algorithm = DEFAULT_OPTIMIZATION_ALGORITHM
    opti_selective_optimization = None              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized

    optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)


def unitTest_Nejc_POKER(allCases) :

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] )  #Celtra All

    testBatch_Tom = BanditTestBatch( allCases, [10] ) # Tom test case
    testBatch_Nejc = BanditTestBatch( allCases, [len(allCases)-1] ) # Nejc test case

    eval_cases = testBatch_Nejc
    eval_repeats = 10
    eval_oracle_probablity = 0

    solv_initial_param_values = [[0, 1]]     #if None: default will be used
    solv_selection_policy = GLODEF_SELECTION_POKER
    solv_change_point_detector = GLODEF_CHANGEPOINT_NONE
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [GLODEF_PARAM_FUNCTION_LINEAR] #[DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [1] #[DEFAULT_PARAM_NUMINPUTS]

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)
    evaluateBatch(solver, eval_cases, eval_repeats, 0, eval_oracle_probablity)

def unitTest_Nejc_UCBT(allCases) :

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] )  #Celtra All

    testBatch_Tom = BanditTestBatch( allCases, [10] ) # Tom test case
    testBatch_Nejc = BanditTestBatch( allCases, [len(allCases)-1] ) # Nejc test case

    eval_cases = testBatch_Nejc
    eval_repeats = 10
    eval_oracle_probablity = 0

    solv_initial_param_values = [0.77]
    solv_selection_policy = GLODEF_SELECTION_UCBTUNED
    solv_change_point_detector = GLODEF_CHANGEPOINT_NONE
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS]
    solv_param_num_inputs = [1] #[DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)
    evaluateBatch(solver, eval_cases, eval_repeats, 0, eval_oracle_probablity)

def unitTest_Nejc_SOFTMAX(allCases) :

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] )  #Celtra All

    testBatch_Tom = BanditTestBatch( allCases, [10] ) # Tom test case
    testBatch_Nejc = BanditTestBatch( allCases, [len(allCases)-1] ) # Nejc test case

    eval_cases = testBatch_Nejc
    eval_repeats = 10
    eval_oracle_probablity = 0

    solv_initial_param_values = [0.1]
    solv_selection_policy = GLODEF_SELECTION_SOFTMAX
    solv_change_point_detector = GLODEF_CHANGEPOINT_NONE
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS]
    solv_param_num_inputs = [1] #[DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)
    evaluateBatch(solver, eval_cases, eval_repeats, 0, eval_oracle_probablity)
