from Config import *
from fileIO import *
from SampleAnalyzer import *
from Jackpot_init import *
from MABsolver import *
from Evaluator import *
from Optimization import *
from unitTests import *



# 2014.10.18 test policies without change point detection on Celtra's testcases
def test_2014_10_20_changePoint_DavorTom2par(allCases):

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, xrange(10) )  #Celtra

    #-- change configuration here

    #opti_learn_cases = testBatch_01_05
    #opti_learn_cases = testBatch_06_10
    opti_learn_cases = testBatch_01_10

    #solv_selection_policy = GLODEF_SELECTION_EGREEDY
    #solv_initial_param_values = [0.140, 2.0, 1.0, 50, 1.0]     #if None: default will be used
    #opti_config_params_lower_bounds = [0.0]
    #opti_config_params_upper_bounds = [0.4]

    #solv_selection_policy = GLODEF_SELECTION_SOFTMAX
    #opti_config_param_boundaries = [0.005, 0.02]       #softmax tao lower boundary must be > 0

    #solv_selection_policy = GLODEF_SELECTION_UCB1
    #solv_initial_param_values = [0.240, 2.0, 1.0, 50, 1.0]     #if None: default will be used

    solv_selection_policy = GLODEF_SELECTION_UCBTUNED
    solv_initial_param_values = [0.770, 2.0, 1.0, 50, 1.0]     #if None: default will be used

    opti_selective_optimization = [0]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    opti_config_params_lower_bounds = [0.0]
    opti_config_params_upper_bounds = [2.5]

    #opti_selective_optimization = [1, 3]              #choosen parameters to optimize - array of indices, if none then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.2, 10]
    #opti_config_params_upper_bounds = [9.9, 300]

    #opti_selective_optimization = [0, 1, 2, 3]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.0, 0.3, 0.4, 10]
    #opti_config_params_upper_bounds = [3.0, 9.9, 1.0, 300]

    #opti_config_grid_step = [0.01, 0.05, 0.01, 10]          # [] - disabled (continuous)
    opti_config_grid_step = []

    #opti_selective_optimization = [1, 2, 3]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.5, 0.5, 10]
    #opti_config_params_upper_bounds = [9.0, 1.0, 300]

    #opti_selective_optimization = [0, 1, 2, 3]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.0, 0.5, 0.5, 10]
    #opti_config_params_upper_bounds = [3.0, 7.0, 1.0, 300]

    #solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_ZERO
    #solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_MOVING_AVERAGE
    solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_MOVING_AVERAGE_CUTOFF
    #solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_TO_MOVING_AVERAGE

    opti_oracle_probablity = 0
    opti_completeRepeats = 100
    
    solv_change_point_detector = GLODEF_CHANGEPOINT_NONE
    #solv_change_point_detector = GLODEF_CHANGEPOINT_DAVORTOM
    #solv_change_point_detector = GLODEF_CHANGEPOINT_HENKYPENKY

    #-- do not change values below here --#

    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)

    opti_solver = solver
    if opti_oracle_probablity == 1 :
        opti_evaluations_per_sample = 1
    else :
        opti_evaluations_per_sample = 100
    opti_config = [     #configuration for the optimization algorithm: arbitrary list of additional parameters
    opti_config_params_lower_bounds,         # lower bounds for all parameters
    opti_config_params_upper_bounds,         # upper bounds for all parameters
    opti_config_grid_step,                 # grid step (if you want discrete search); leave empty for continuous search
    int(sqrt(len(opti_selective_optimization)))*10,                 # number of cycles (epochs) of SA
    int(sqrt(len(opti_selective_optimization)))*10,                 # number of iterations per each cycle
    0.75,               # probability of accepting worse solution at the start
    0.01,               # probability of accepting worse solution at the end
    0.50,               # neighbourhood radius at the start (ratio of interval)
    0.01                # neighbourhood radius at the end (ratio of interval)
    ]
    opti_algorithm = GLODEF_OPTIMIZATION_ANNEALING
    opti_fitness_metric = GLODEF_FITNESS_OPTIMALITY_RANDNOR


    optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)

    opti_suppress_output = 0

    optimizer.Optimize(opti_learn_cases, opti_config, opti_completeRepeats, opti_suppress_output, opti_oracle_probablity)

def test_2014_10_20_HankeyPankey_treshold(allCases):

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, xrange(10) )  #Celtra

    #-- change configuration here

    #opti_learn_cases = testBatch_01_05
    #opti_learn_cases = testBatch_06_10
    opti_learn_cases = testBatch_01_10

    #solv_selection_policy = GLODEF_SELECTION_EGREEDY
    #solv_initial_param_values = [0.140, 2.0, 1.0, 50, 1.0]     #if None: default will be used
    ##opti_config_param_boundaries = [0.0, 0.4]

    #solv_selection_policy = GLODEF_SELECTION_SOFTMAX
    #opti_config_param_boundaries = [0.005, 0.02]       #softmax tao lower boundary must be > 0

    #solv_selection_policy = GLODEF_SELECTION_UCB1
    #solv_initial_param_values = [0.240, 2.0, 1.0, 50, 1.0]     #if None: default will be used

    solv_selection_policy = GLODEF_SELECTION_UCBTUNED
    solv_initial_param_values = [0.770, 10.0, 1.0, 50, 1.0]     #if None: default will be used

    #opti_selective_optimization = [1]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.2]
    #opti_config_params_upper_bounds = [9.9]

    opti_selective_optimization = [1, 2]              #choosen parameters to optimize - array of indices, if none then all parameters will be optimized
    opti_config_params_lower_bounds = [5, 10]
    opti_config_params_upper_bounds = [150, 500]

    #opti_selective_optimization = [0, 1, 2, 3]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.0, 0.3, 0.4, 10]
    #opti_config_params_upper_bounds = [3.0, 9.9, 1.0, 300]

    #opti_config_grid_step = [0.01, 0.05, 0.01, 10]          # [] - disabled (continuous)
    opti_config_grid_step = []

    #opti_selective_optimization = [1, 2, 3]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.5, 0.5, 10]
    #opti_config_params_upper_bounds = [9.0, 1.0, 300]

    #opti_selective_optimization = [0, 1, 2, 3]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized
    #opti_config_params_lower_bounds = [0.0, 0.5, 0.5, 10]
    #opti_config_params_upper_bounds = [3.0, 7.0, 1.0, 300]

    #solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_ZERO
    #solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_MOVING_AVERAGE
    #solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_MOVING_AVERAGE_CUTOFF
    solv_reset_algorithm = GLODEF_RESET_ALGORITHM_RESET_TO_MOVING_AVERAGE

    opti_oracle_probablity = 0
    opti_completeRepeats = 100

    #-- do not change values below here --#

    solv_change_point_detector = GLODEF_CHANGEPOINT_HENKYPENKY
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)

    opti_solver = solver
    if opti_oracle_probablity == 1 :
        opti_evaluations_per_sample = 1
    else :
        opti_evaluations_per_sample = 10
    opti_config = [     #configuration for the optimization algorithm: arbitrary list of additional parameters
    opti_config_params_lower_bounds,         # lower bounds for all parameters
    opti_config_params_upper_bounds,         # upper bounds for all parameters
    opti_config_grid_step,                 # grid step (if you want discrete search); leave empty for continuous search
    int(sqrt(len(opti_selective_optimization)))*10,                 # number of cycles (epochs) of SA
    int(sqrt(len(opti_selective_optimization)))*10,                 # number of iterations per each cycle
    0.75,               # probability of accepting worse solution at the start
    0.01,               # probability of accepting worse solution at the end
    0.50,               # neighbourhood radius at the start (ratio of interval)
    0.01                # neighbourhood radius at the end (ratio of interval)
    ]
    opti_algorithm = GLODEF_OPTIMIZATION_ANNEALING
    opti_fitness_metric = GLODEF_FITNESS_OPTIMALITY_RANDNOR


    optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)

    opti_suppress_output = 0

    optimizer.Optimize(opti_learn_cases, opti_config, opti_completeRepeats, opti_suppress_output, opti_oracle_probablity)

# 2014.10.18 test policies without change point detection on Celtra's testcases
def test_2014_10_18_noChangePoint(allCases):

    testBatch_Complete = BanditTestBatch( allCases, xrange(len(allCases)) ) #All
    testBatch_01_05 = BanditTestBatch( allCases, [0, 1, 2, 3, 4] )  #Celtra
    testBatch_06_10 = BanditTestBatch( allCases, [5, 6, 7, 8, 9] )  #Celtra
    testBatch_01_10 = BanditTestBatch( allCases, xrange(10) )  #Celtra

    #-- change configuration here

    #opti_learn_cases = testBatch_01_05
    opti_learn_cases = testBatch_06_10
    #opti_learn_cases = testBatch_01_10

    solv_selection_policy = GLODEF_SELECTION_EGREEDY
    opti_config_param_boundaries = [0.0, 0.4]

    #solv_selection_policy = GLODEF_SELECTION_SOFTMAX
    #opti_config_param_boundaries = [0.005, 0.02]       #softmax tao lower boundary must be > 0

    ##solv_selection_policy = GLODEF_SELECTION_UCB1
    #solv_selection_policy = GLODEF_SELECTION_UCBTUNED
    #opti_config_param_boundaries = [0.0, 3.0]

    opti_oracle_probablity = 0
    opti_completeRepeats = 100

    #-- do not change values below here

    solv_initial_param_values = None     #if None: default will be used
    solv_change_point_detector = GLODEF_CHANGEPOINT_NONE
    solv_change_point_test = DEFAULT_CHANGEPOINT_TEST
    solv_reset_algorithm = DEFAULT_RESET_ALGORITHM
    solv_param_types = [DEFAULT_PARAM_FUNCTIONS] * DEFAULT_SOLVER_NUMPARAMS
    solv_param_num_inputs = [DEFAULT_PARAM_NUMINPUTS] * DEFAULT_SOLVER_NUMPARAMS

    solver = MABsolver(solv_initial_param_values, solv_selection_policy, solv_change_point_detector, solv_change_point_test, solv_reset_algorithm, solv_param_types, solv_param_num_inputs)

    opti_solver = solver
    if opti_oracle_probablity == 1 :
        opti_evaluations_per_sample = 5
    else :
        opti_evaluations_per_sample = 25
    opti_config = [     #configuration for the optimization algorithm: arbitrary list of additional parameters
    [opti_config_param_boundaries[0]],         # lower bounds for all parameters
    [opti_config_param_boundaries[1]],         # upper bounds for all parameters
    [],                 # grid step (if you want discrete search); leave empty for continuous search
    10,                 # number of cycles (epochs) of SA
    10,                 # number of iterations per each cycle
    0.75,               # probability of accepting worse solution at the start
    0.01,               # probability of accepting worse solution at the end
    0.50,               # neighbourhood radius at the start (ratio of interval)
    0.01                # neighbourhood radius at the end (ratio of interval)
    ]

    opti_fitness_metric = GLODEF_FITNESS_OPTIMALITY_RANDNOR
    opti_algorithm = GLODEF_OPTIMIZATION_ANNEALING
    opti_selective_optimization = [0]              #choosen parameters to optimize - array of indices, if None then all parameters will be optimized

    optimizer = Optimizer(opti_solver, opti_evaluations_per_sample, opti_config, opti_fitness_metric, opti_algorithm, opti_selective_optimization)

    opti_suppress_output = 0

    optimizer.Optimize(opti_learn_cases, opti_config, opti_completeRepeats, opti_suppress_output, opti_oracle_probablity)
