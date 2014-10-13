from configuration import *
from changePointDetection import *
from machine import *
from strategy import *

# ------------------------------------- #


def evaluation_single_case(
    case, 
    suppress_output, 
    selected_algorithms,
    input_params,
    function_approximator
    ) :      
    
    #algorithm selection
    selection_algorithm = selected_algorithms[0]
    change_point_algorithm = selected_algorithms[1]
    reset_algorithm = selected_algorithms[2]

    #learning parameters
    epsilon_soft = input_params[0]
    softMax_tao = input_params[1]
    UCB1_parC = input_params[2]
    change_point_threshold = input_params[3]

    #init memory structures
    machines = [machine(m) for m in range(case.numBandits)]

    #init global variables
    total_rejected_pulls = 0
    rejected_pulls = 0

    #execute play
    for p in range(0,case.maxPulls) :

        if not (function_approximator == GLODEF_FUNCTION_APPROX_NONE) :
            approximator_input1 = case.numBandits
            approximator_input2 = case.maxPulls - total_rejected_pulls
            approximator_input3 = p
            approximator_input4 = p - total_rejected_pulls
            UCB1_parC = function_approximator(approximator_input1, approximator_input2, approximator_input3, approximator_input4)
            epsilon_soft = function_approximator(approximator_input1, approximator_input2, approximator_input3, approximator_input4)
            change_point_threshold = function_approximator(approximator_input1, approximator_input2, approximator_input3, approximator_input4)
            softMax_tao = function_approximator(approximator_input1, approximator_input2, approximator_input3, approximator_input4)

        #choose bandit/machine
        if  selection_algorithm == GLODEF_SELECTION_RANDOM:
            selected_machine = machines[random.randint(0,case.numBandits - 1)]
        elif selection_algorithm == GLODEF_SELECTION_EGREEDY :
            selected_machine = EGreedy(machines,epsilon_soft)
        elif selection_algorithm == GLODEF_SELECTION_SOFTMAX :
            selected_machine = softMax(machines, softMax_tao)
        elif selection_algorithm == GLODEF_SELECTION_UCB1 :
            selected_machine = UCB1(machines, p - total_rejected_pulls, UCB1_parC)
        elif selection_algorithm == GLODEF_SELECTION_UCB1TUNED :
            selected_machine = UCBT(machines, p - total_rejected_pulls, UCB1_parC)
        
        #get reward
        last_reward = case.pullBandit(selected_machine.id, p)

        #update statistics
        selected_machine.update(last_reward)

        #change point detection
        if change_point_algorithm == GLODEF_CHANGEPOINT_DAVORTOM :
            rejected_pulls = checkChange(change_point_threshold, selected_machine, reset_algorithm)
            #TODO: in checkChange() implement different kinds of reset_algorithm (put it out of checkChange()), input gets selected_machine
            total_rejected_pulls = total_rejected_pulls + rejected_pulls
            if rejected_pulls > 0 :
                if not suppress_output :
                    print 'Global pull  at change point:' + str(i)

        elif change_point_algorithm == GLODEF_CHANGEPOINT_HENKYPENKY :
            #todo henky penky
            todo

    #sum of collected reward
    total_reward = 0.0
    for m in machines:
        total_reward = total_reward + m.sum_total
        if not suppress_output:
            print 'Machine '+str(m.id)+' Total reward: '+str(m.sum_total)+' Total pulls: '+str(m.pulls_total)+' Average reward: '+str(machines.mean)

    if not suppress_output:
        print 'Total reward: '+str(total_reward)+' maximum possible reward: '+str(case.maximumReward)

    return total_reward


def evaluation_batch_cases(
    cases,
    repeats,
    suppress_output = 0, 
    selected_algorithms = [DEFAULT_SELECTION_ALGORITHM, DEFAULT_CHANGEPOINT_ALGORITHM, DEFAULT_RESET_ALGORITHM], 
    input_params = [DEFAULT_PAR_EGREEDY_E, DEFAULT_PAR_SOFTMAX_T, DEFAULT_PAR_UCB1_C, DEFAULT_PAR_CHANGEPOINT_THR], 
    function_approximator = GLODEF_FUNCTION_APPROX_NONE
    ) :

    #define metrics output format
    metrics_labels = ["        SumR","      Regret","  Optimality [%]"]
    metrics_out = ["    %8.2f","    %8.2f","          %6.2f"]

    #init
    num_cases = len(cases)

    #compute maximal possible sum of rewards and random policy performance
    summedMaxRewards = 0.0
    summedRandomRewards = 0.0
    for c in xrange(0,num_cases) :
        summedMaxRewards += cases[c].maximumReward
        summedRandomRewards += cases[c].randomReward

    #init performance metrics
    num_metrics = 3
        #0 - sum of rewards
        #1 - regret
        #2 - optimality factor (sum of rewards divided by maximum possible reward) in %

    metrics = [[0.0 for x in xrange(num_cases)] for x in xrange(num_metrics)]
    avg_metrics = [0.0 for x in xrange(num_metrics)]
    new_avg_metrics = [0.0 for x in xrange(num_metrics)]
    new_metrics = [0.0 for x in xrange(num_metrics)]

    #user output
    if not suppress_output :
        print 'Procedure evaluation_artificial_cases()'
        print 'Settings: %s , %s , %s , %s' % (
            GLO_labels_selection_algorithms[selected_algorithms[0]], 
            GLO_labels_change_point_detectors[selected_algorithms[1]], 
            GLO_labels_reset_algorithms[selected_algorithms[2]], 
            GLO_labels_function_approx[function_approximator] 
            )
        print 'Param values %f %f %f %f' % (input_params[0], input_params[1], input_params[2], input_params[3])
        print 'Case list: ',
        for i in xrange(num_cases) :
            print '%d ' % cases[i].ID
        print 'Total cases: ' + str(num_cases)
        print 'Maximum summed reward: ' + str(summedMaxRewards)
        print 'Random reward: ' + str(summedRandomRewards)
        print 'Total repeats: ' + str(repeats)
        print ''
        print 'rep    ',
        for i in xrange(num_metrics):
            print metrics_labels[i],
        print ''

    #evaluate all cases
    for r in xrange(repeats) :

        #reset averaged (through cases) metrics
        for i in xrange(num_metrics):
            new_avg_metrics[i] = 0.0
        
        for c in xrange(0,num_cases) :
            #execute bandit game (case)
            new_result = evaluation_single_case(cases[c], 1, selected_algorithms, input_params, function_approximator)

            #update results by different metrics
            new_metrics[0] = new_result
            new_metrics[1] = (cases[c].maximumReward - new_result)
            new_metrics[2] = new_result / cases[c].maximumReward * 100.0
            for i in xrange(num_metrics):
                metrics[i][c] +=  (1.0/(r+1.0))*(new_metrics[i] - metrics[i][c])
                new_avg_metrics[i] += new_metrics[i]

        #calculate overall performance
        new_avg_metrics[2] /= num_cases
        if not suppress_output :
            print ('%5d  ') % r,
        for i in xrange(num_metrics):
            avg_metrics[i]  += (1.0/(r+1.0))*(new_avg_metrics[i] - avg_metrics[i])
            if not suppress_output :
                print (metrics_out[i]) % (avg_metrics[i]),
        if not suppress_output :
            print ''
        
    #returns
    #   measurements averaged over all cases
    #   measurements for each case individually
    return (avg_metrics, metrics)
