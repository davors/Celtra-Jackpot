from GlobalDefines import *

#set to 1 if test
#set to 0 if production
TEST = 1

#number of test cases
N_CASES = 10

#server
server='celtra-jackpot.com'

#default settings (for possible options see GlobalDefines.py)
DEFAULT_SELECTION_ALGORITHM = GLODEF_SELECTION_UCB1TUNED
    #GLODEF_SELECTION_RANDOM = 0
    #GLODEF_SELECTION_EGREEDY = 1
    #GLODEF_SELECTION_SOFTMAX = 2
    #GLODEF_SELECTION_UCB1 = 3
    #GLODEF_SELECTION_UCB1TUNED = 4

DEFAULT_CHANGEPOINT_ALGORITHM = GLODEF_CHANGEPOINT_NONE
    #GLODEF_CHANGEPOINT_NONE = 0
    #GLODEF_CHANGEPOINT_DAVORTOM = 1
    #GLODEF_CHANGEPOINT_HENKYPENKY = 2

DEFAULT_RESET_ALGORITHM = GLODEF_RESET_ALGORITHM_TODO
    #GLODEF_RESET_ALGORITHM_TODO = 0

DEFAULT_OPTIMIZATION_ALGORITHM = GLODEF_OPTIMIZATION_ANNEALING
    #GLODEF_OPTIMIZATION_ANNEALING = 0
    #GLODEF_OPTIMIZATION_GENETIC = 1

DEFAULT_FITNESS_METRIC = GLODEF_FITNESS_SUMREWARDS
    #GLODEF_FITNESS_SUMREWARDS = 0
    #GLODEF_FITNESS_REGRET = 1
    #GLODEF_FITNESS_OPTIMALITY = 2

DEFAULT_FUNCTION_APPROXIMATOR = GLODEF_FUNCTION_APPROX_NONE
    #GLODEF_FUNCTION_APPROX_NONE = None
    #GLODEF_FUNCTION_APPROX_DIRECT = 1
    #GLODEF_FUNCTION_APPROX_LINEAR = 2
    #GLODEF_FUNCTION_APPROX_NEURAL = 3

DEFAULT_PAR_EGREEDY_E = 0.1
DEFAULT_PAR_SOFTMAX_T = 0.01
DEFAULT_PAR_UCB1_C = 1.0
DEFAULT_PAR_CHANGEPOINT_THR = 2.5