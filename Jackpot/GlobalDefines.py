#defines

GLODEF_SELECTION_RANDOM = 0
GLODEF_SELECTION_EGREEDY = 1
GLODEF_SELECTION_SOFTMAX = 2
GLODEF_SELECTION_UCB1 = 3
GLODEF_SELECTION_UCB1TUNED = 4

GLODEF_CHANGEPOINT_NONE = 0
GLODEF_CHANGEPOINT_DAVORTOM = 1
GLODEF_CHANGEPOINT_HENKYPENKY = 2

#TODO !!!
GLODEF_RESET_ALGORITHM_TODO = 0
#TODO !!!

GLODEF_OPTIMIZATION_ANNEALING = 0
GLODEF_OPTIMIZATION_ANNEALING = 1

GLODEF_FITNESS_SUMREWARDS = 0
GLODEF_FITNESS_REGRET = 1
GLODEF_FITNESS_OPTIMALITY = 2

GLODEF_FUNCTION_APPROX_NONE = 0
GLODEF_FUNCTION_APPROX_DIRECT = 1
GLODEF_FUNCTION_APPROX_LINEAR = 2
GLODEF_FUNCTION_APPROX_NEURAL = 3

GLO_labels_selection_algorithms = [
    'random',
    'epsilonGreedy',
    'softMax',
    'UCB1',
    'UCBtuned'
    ]

GLO_labels_change_point_detectors = [
    'CP: Disabled',
    'DavorTom',
    'HenkyPenky'
    ]
GLO_labels_reset_algorithms = [
    'Reset: TODO'
    ]

GLO_labels_optimization = [
    "simulated annealing",
    "genetic algorithm"
    ]

GLO_labels_metrics = [
    "Sum rewards",
    "Regret",
    "Optimality [%%]"
    ]

GLO_labels_function_approx = [
    "Aprox: disabled",
    "Aprox: Direct",
    "Aprox: Linear",
    "Aprox: Neural"
    ]

