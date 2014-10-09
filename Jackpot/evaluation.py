from changePointDetection import *
from machine import *
from strategy import *

def evaluation_batch_cases(cases, repeats) :

    #define metrics output format
    metrics_labels = ["        SumR","      Regret","  Optimality [%]"]
    metrics_out = ["    %8.2f","    %8.2f","         %6.2f"]

    #init
    num_cases = len(cases)

    #compute maximal possible sum of rewards and random policy performance
    maxRewards = [0.0 for x in xrange(num_cases)]
    randomRewards = [0.0 for x in xrange(num_cases)]
    summedMaxRewards = 0.0
    summedRandomRewards = 0.0
    for c in xrange(0,num_cases) :
        maxRewards[c] = cases[c].calcMaxReward()
        randomRewards[c] = cases[c].calcRandomReward()
        summedMaxRewards += maxRewards[c]
        summedRandomRewards += randomRewards[c]

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
            new_result = evaluation_single_case(cases[c], 0)

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
        

def evaluation_single_case(case, print_output = 1) :      
    
    #learning parameters
    UCB1_parC = 1.0
    epsilon_soft = 0.1
    change_point_threshold = 2.5

    #init memory structures
    machines = [machine(m) for m in range(case.numBandits)]

    #init global variables
    total_rejected_pulls = 0

    #execute play
    for p in range(0,case.maxPulls) :

        #choose bandit/machine
        selected_machine = UCB1(machines, p - total_rejected_pulls, UCB1_parC)
        #selected_machine = EGreedy(machines,epsilon_soft)

        #get reward
        last_reward = case.pullBandit(selected_machine.id, p)

        #update statistics
        selected_machine.update(last_reward)

        #change point detection
        rejected_pulls = checkChange(change_point_threshold, selected_machine)
        total_rejected_pulls = total_rejected_pulls + rejected_pulls
        if rejected_pulls > 0 :
            if print_output :
                print 'Global pull  at change point:'+str(i)

    #sum of collected reward
    total_reward = 0.0
    for m in machines:
        total_reward = total_reward + m.sum_total
        if print_output :
            print 'Machine '+str(m.id)+' Total reward: '+str(m.sum_total)+' Total pulls: '+str(m.pulls_total)+' Average reward: '+str(m.mean)

    if print_output:
        print 'Total reward: '+str(totalReward)+' maximum possible reward: '+str(maxReward)

    return total_reward
