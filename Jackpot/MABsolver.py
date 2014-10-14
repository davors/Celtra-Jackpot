from configuration import *
from machine import *
from strategy import *
from changePointDetection import *

# configuration structure for MABsolver
class MABsolver_config():

    selectionPolicy = None
    changePointDetector = None
    changePointTest = None
    resetAlgorithm = None
    params = None
    approximator = None

    def __init__(self, 
        selectionPolicy = DEFAULT_SELECTION_POLICY, 
        changePointDetector = DEFAULT_CHANGEPOINT_DETECTOR, 
        changePointTest = DEFAULT_CHANGEPOINT_TEST,
        resetAlgorithm = DEFAULT_RESET_ALGORITHM,
        params = [DEFAULT_PAR_EGREEDY_E, DEFAULT_PAR_SOFTMAX_T, DEFAULT_PAR_UCB1_C, DEFAULT_PAR_CHANGEPOINT_THR],
        approximator = GLODEF_FUNCTION_APPROX_NONE
        ) :

        self.selectionPolicy = selectionPolicy
        self.changePointDetector = changePointDetector
        self.resetAlgorithm = resetAlgorithm
        self.changePointTest = changePointTest
        self.params = params
        self.approximator = approximator

    def info(self) :
        print 'MABsolver_config: algorithms: %s , %s , %s , %s , %s' % (
            GLO_labels_selection_policies[self.selectionPolicy], 
            GLO_labels_change_point_detectors[self.changePointDetector], 
            GLO_labels_change_point_test[self.changePointTest],
            GLO_labels_reset_algorithms[self.changePointTest], 
            GLO_labels_function_approx[self.approximator] 
            )
        print 'MABsolver_config: params:    ',
        for i in range(len(self.params)) :
            print '%f ' % self.params[i],
        print '' 

# The Multi-Armed-Bandit (MAB) solver structure
class MABsolver():

    config = None
    machines = None
    numMachines = None

    pulls = None
    total_rejected_pulls = None

    epsilon_soft = None
    softMax_tao = None
    UCB1_parC = None
    change_point_threshold = None

    # initialization
    def __init__(
        self, 
        num_bandits = 0,
        selectionPolicy = DEFAULT_SELECTION_POLICY, 
        changePointDetector = DEFAULT_CHANGEPOINT_DETECTOR, 
        changePointTest = DEFAULT_CHANGEPOINT_TEST,
        resetAlgorithm = DEFAULT_RESET_ALGORITHM,
        params = [DEFAULT_PAR_EGREEDY_E, DEFAULT_PAR_SOFTMAX_T, DEFAULT_PAR_UCB1_C, DEFAULT_PAR_CHANGEPOINT_THR],
        approximator = GLODEF_FUNCTION_APPROX_NONE
        ) :
        
        self.config = MABsolver_config(selectionPolicy, changePointDetector, changePointTest, resetAlgorithm, params, approximator)
        self.resetState(num_bandits)

    # reset memory structures (preparation for new testcase)
    def resetState(self, num_bandits) :
        self.machines = [machine(m) for m in range(num_bandits)]
        self.numMachines = num_bandits

        self.pulls = 0
        self.total_rejected_pulls = 0

        self.epsilon_soft = self.config.params[0]
        self.softMax_tao = self.config.params[1]
        self.UCB1_parC = self.config.params[2]
        self.change_point_threshold = self.config.params[3]

    # select a bandit from available stats
    def selectBandit(self, increase_pulls = 1) :

        if   self.config.selectionPolicy == GLODEF_SELECTION_RANDOM:    selected_machine = self.machines[random.randint(0, self.numMachines - 1)]
        elif self.config.selectionPolicy == GLODEF_SELECTION_EGREEDY :  selected_machine = EGreedy(self.machines, self.epsilon_soft)
        elif self.config.selectionPolicy == GLODEF_SELECTION_SOFTMAX :  selected_machine = softMax(self.machines, self.softMax_tao)
        elif self.config.selectionPolicy == GLODEF_SELECTION_UCB1 :     selected_machine = UCB1(self.machines, self.pulls - self.total_rejected_pulls, self.UCB1_parC)
        elif self.config.selectionPolicy == GLODEF_SELECTION_UCBTUNED : selected_machine = UCBT(self.machines, self.pulls - self.total_rejected_pulls, self.UCB1_parC)

        self.pulls += increase_pulls

        return selected_machine.id


    # update stats and detect change point (if enabled)
    def update(self, machine_id, reward, suppress_output = 0) :

        self.machines[machine_id].update(reward)

        # change point detection
        rejected_pulls = 0

        if self.config.changePointDetector == GLODEF_CHANGEPOINT_DAVORTOM :
            rejected_pulls = checkChange(self.change_point_threshold, self.machines[machine_id], self.config.resetAlgorithm)
            #TODO: in checkChange() implement different kinds of reset_algorithm (put it out of checkChange()), input gets selected_machine
            self.total_rejected_pulls = self.total_rejected_pulls + rejected_pulls
            if rejected_pulls > 0 :
                if not suppress_output :
                    print 'MABsolver: changePointDetector: Global pull at change point: %d' + i

        elif self.config.changePointDetector == GLODEF_CHANGEPOINT_HENKYPENKY :
            #todo henky penky
            todo

        self.total_rejected_pulls += rejected_pulls


    # output memorized stats
    def infoStats(self) :
        for m in self.machines:
                print 'MABsolver_stats: Machine '+str(m.id)+' Total reward: '+str(m.sum_total)+' Total pulls: '+str(m.pulls_total)+' Average reward: '+str(m.mean)
