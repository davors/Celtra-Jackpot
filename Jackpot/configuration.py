from GlobalDefines import *
from Config_testCases import *

#set to 1 if test
#set to 0 if production
TEST = 1

#number of test cases
N_CASES = 10

#server
server='celtra-jackpot.com'

#default settings (for possible options see GlobalDefines.py)
DEFAULT_SELECTION_POLICY = GLODEF_SELECTION_UCBTUNED
    #GLODEF_SELECTION_RANDOM = 0
    #GLODEF_SELECTION_EGREEDY = 1
    #GLODEF_SELECTION_SOFTMAX = 2
    #GLODEF_SELECTION_UCB1 = 3
    #GLODEF_SELECTION_UCBTUNED = 4

DEFAULT_CHANGEPOINT_DETECTOR = GLODEF_CHANGEPOINT_NONE
    #GLODEF_CHANGEPOINT_NONE = 0
    #GLODEF_CHANGEPOINT_DAVORTOM = 1
    #GLODEF_CHANGEPOINT_HENKYPENKY = 2

DEFAULT_CHANGEPOINT_TEST = GLODEF_CHANGEPOINT_TEST_DAVOR
    #GLODEF_CHANGEPOINT_TEST_DAVOR = 0
    #GLODEF_CHANGEPOINT_TEST_TOM = 1

DEFAULT_RESET_ALGORITHM = GLODEF_RESET_ALGORITHM_RESET_ALL_TO_ZERO
    #GLODEF_RESET_ALGORITHM_TODO = 0

DEFAULT_OPTIMIZATION_ALGORITHM = GLODEF_OPTIMIZATION_ANNEALING
    #GLODEF_OPTIMIZATION_ANNEALING = 0
    #GLODEF_OPTIMIZATION_GENETIC = 1

DEFAULT_FITNESS_METRIC = GLODEF_FITNESS_SUMREWARDS
    #GLODEF_FITNESS_SUMREWARDS = 0
    #GLODEF_FITNESS_REGRET = 1
    #GLODEF_FITNESS_OPTIMALITY = 2

DEFAULT_PARAM_FUNCTIONS = GLODEF_PARAM_FUNCTION_DIRECT
    #GLODEF_PARAM_FUNCTION_DIRECT = 0
    #GLODEF_PARAM_FUNCTION_LINEAR = 1
    #GLODEF_PARAM_FUNCTION_NEURAL = 2

DEFAULT_SOLVER_NUMPARAMS = 4
    # one parameter for selection algorithm, three parameters for change point detector
DEFAULT_PARAM_NUMINPUTS = 0
    # number of parameter function internal weights (stored values) are number of inputs + 1

DEFAULT_PAR_EGREEDY_E = 0.1         # epsilon-greedy parameter: Epsilon
DEFAULT_PAR_SOFTMAX_T = 0.01        # softMax parameter: tau
DEFAULT_PAR_UCB1_C = 1.0            # UCB parameter: C
DEFAULT_PAR_CHANGEPOINT_THR = 2.5   # change point detector parameter: Z-Threshold
DEFAULT_PAR_CHANGEPOINT_INT = 0.2   # change point detector parameter: interval shrink (e.g., 0.2 translates interval [0,1] to [0.2,0.8]
DEFAULT_PAR_CHANGEPOINT_NUM = 5     # change point detector parameter: lowest number of moving average samples that may trigger reset
