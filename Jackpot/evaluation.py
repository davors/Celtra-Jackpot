from changePointDetection import *
from machine import *
from strategy import *

# ------------------------------------- #

selection_algorithms = [
    'random',
    'epsilonGreedy'
    'softMax',
    'UCB1',
    'UCBtuned'
    ]

change_point_detectors = [
    'none',
    'DavorTom',
    'HenkyPenky'
    ]

def evaluation_single_case(case, suppress_output = 0) :      
    
    #algorithm selection
    selection_algorithm = 0
        # 0 'random'
        # 1 'epsilonGreedy
        # 2 'softMax'
        # 3 'UCB1'
        # 4 'UCBtuned'
    change_point_algorithm = 'none'
        # 0 'none'
        # 1 'DavorTom'
        # 2 'HenkyPenky'

    #learning parameters
    UCB1_parC = 1.0
    epsilon_soft = 0.1
    change_point_threshold = 2.5

    #init memory structures
    machines = [machine(m) for m in range(case.numBandits)]

    #init global variables
    total_rejected_pulls = 0
    rejected_pulls = 0

    #execute play
    for p in range(0,case.maxPulls) :

        #choose bandit/machine
        if  selection_algorithm == 0:
            selected_machine = machines[random.randint(0,case.numBandits-1)]
        elif selection_algorithm == 1 :
            selected_machine = EGreedy(machines,epsilon_soft)
        elif selection_algorithm == 2 :
            todo
        elif selection_algorithm == 3 :
            selected_machine = UCB1(machines, p - total_rejected_pulls, UCB1_parC)
        elif selection_algorithm == 4 :
            selected_machine = UCBT(machines, p - total_rejected_pulls, UCB1_parC)
        
        #get reward
        last_reward = case.pullBandit(selected_machine.id, p)

        #update statistics
        selected_machine.update(last_reward)

        #change point detection
        if change_point_algorithm == 1 :
            rejected_pulls = checkChange(change_point_threshold, selected_machine)
            total_rejected_pulls = total_rejected_pulls + rejected_pulls
            if rejected_pulls > 0 :
                if not suppress_output :
                    print 'Global pull  at change point:'+str(i)

        elif change_point_algorithm == 2:
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


def evaluation_batch_cases(cases, repeats) :

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
    print 'Procedure evaluation_artificial_cases()'
    #print 'Case list: ' + case_list
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
            new_result = evaluation_single_case(cases[c], 1)

            #update results by different metrics
            new_metrics[0] = new_result
            new_metrics[1] = (cases[c].maximumReward - new_result)
            new_metrics[2] = new_result / cases[c].maximumReward * 100.0
            for i in xrange(num_metrics):
                metrics[i][c] +=  (1.0/(r+1.0))*(new_metrics[i] - metrics[i][c])
                new_avg_metrics[i] += new_metrics[i]

        #calculate overall performance
        new_avg_metrics[2] /= num_cases
        print ('%5d  ') % r,
        for i in xrange(num_metrics):
            avg_metrics[i]  += (1.0/(r+1.0))*(new_avg_metrics[i] - avg_metrics[i])
            print (metrics_out[i]) % (avg_metrics[i]),
        print ''
        
