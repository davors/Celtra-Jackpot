#defines

GLODEF_SELECTION_RANDOM = 0
GLODEF_SELECTION_EGREEDY = 1
GLODEF_SELECTION_SOFTMAX = 2
GLODEF_SELECTION_UCB1 = 3
GLODEF_SELECTION_UCBTUNED = 4

GLODEF_CHANGEPOINT_NONE = 0
GLODEF_CHANGEPOINT_PERIODICRESET = 1
GLODEF_CHANGEPOINT_DAVORTOM = 2
GLODEF_CHANGEPOINT_HENKYPENKY = 3

GLODEF_CHANGEPOINT_TEST_DAVOR = 0
GLODEF_CHANGEPOINT_TEST_TOM = 1

GLODEF_RESET_ALGORITHM_RESET_ALL_TO_ZERO = 0
GLODEF_RESET_ALGORITHM_RESET_ALL_TO_MOVING_AVERAGE = 1
GLODEF_RESET_ALGORITHM_RESET_ALL_TO_MOVING_AVERAGE_CUTOFF = 2
GLODEF_RESET_ALGORITHM_RESET_TO_MOVING_AVERAGE = 3

GLODEF_OPTIMIZATION_ANNEALING = 0
GLODEF_OPTIMIZATION_GENETIC = 1
GLODEF_OPTIMIZATION_EXHAUSTIVE = 2
GLODEF_OPTIMIZATION_RANDOM = 3

GLODEF_FITNESS_SUMREWARDS = 0
GLODEF_FITNESS_REGRET = 1
GLODEF_FITNESS_OPTIMALITY = 2
GLODEF_FITNESS_OPTIMALITY_RANDNOR = 3

GLODEF_PARAM_FUNCTION_DIRECT = 0
GLODEF_PARAM_FUNCTION_LINEAR = 1
GLODEF_PARAM_FUNCTION_NEURAL = 2

GLO_labels_selection_policies = [
    'Random',
    'EpsGreedy',
    'SoftMax',
    'UCB1',
    'UCBtuned'
    ]

GLO_labels_change_point_detectors = [
    'CP Disabled',
    'CP PeriodicReset',
    'CP DavorTom',
    'CP HenkyPenky'
    ]

GLO_labels_change_point_test = [
    'CPT Davor',
    'CPT Tom'
    ]

GLO_labels_reset_algorithms = [
    'Reset: TODO'
    ]

GLO_labels_optimization = [
    'Simulated Annealing',
    'Genetic',
    'Exhaustive',
    'Random'
    ]

GLO_labels_metrics = [
    'Sum rewards',
    'Regret',
    'Optimality [%]',
    'Random-normalized optimality [%]'
    ]

GLO_shortLabels_metrics = [
    '   SumRew',
    '   Regret',
    '   Opt[%]',
    ' RNopt[%]'
    ]

GLO_metrics_out_format = [
    '  %7.2f',
    '  %7.2f',
    '  %7.2f',
    '  %7.2f'
    ]

GLO_labels_param_function = [
    'Direct',
    'Linear',
    'Neural'
    ]

def PrintStrings(L):
    if isinstance(str(L), basestring):
        print str(L)
    else:
        for x in L:
            PrintStrings(x)
