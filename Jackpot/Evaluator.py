from Config import *
from MABsolver import *
from BanditGenerator import *

def evaluateSingleCase(case, solver, suppress_output = 0) :

    #init solver
    solver.resetState(case.numBandits)

    #init stats
    total_reward = 0.0

    #compute single case evaluation
    for p in xrange(case.maxPulls) :
        selected_bandit = solver.selectBandit()         #apply selection policy
        reward = case.pullBandit(selected_bandit, p)    #get reward
        solver.update(selected_bandit, reward, 1)     #update solver stats
        total_reward += reward                          #sum of collected reward

    #output stats
    if not suppress_output:
        solver.infoStats()
        print 'Total reward: '+str(total_reward)+' maximum possible reward: '+str(case.maximumReward)

    return total_reward

def evaluateBatch(
    solver,
    batch,
    repeats,
    suppress_output = 0
    ) :

    #define metrics output format
    metrics_labels = ["        SumR","      Regret","  Optimality [%]"]
    metrics_out = ["    %8.2f","    %8.2f","          %6.2f"]

    #init performance metrics
    num_metrics = 3
        #0 - sum of rewards
        #1 - regret
        #2 - optimality factor (sum of rewards divided by maximum possible reward) in %

    metrics = [[0.0 for x in xrange(batch.num)] for x in xrange(num_metrics)]
    avg_metrics = [0.0 for x in xrange(num_metrics)]
    new_avg_metrics = [0.0 for x in xrange(num_metrics)]
    new_metrics = [0.0 for x in xrange(num_metrics)]

    #user output
    if not suppress_output :
        print 'Procedure evaluateBatch()'
        solver.config.info()
        batch.info()
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
        
        for c in xrange(0,batch.num) :
            #execute bandit game (case)
            new_result = evaluateSingleCase(batch.list[c], solver, 1)

            #update results by different metrics
            new_metrics[0] = new_result
            new_metrics[1] = (batch.list[c].maximumReward - new_result)
            new_metrics[2] = new_result / batch.list[c].maximumReward * 100.0
            for i in xrange(num_metrics):
                metrics[i][c] +=  (1.0/(r+1.0))*(new_metrics[i] - metrics[i][c])
                new_avg_metrics[i] += new_metrics[i]

        #calculate overall performance
        new_avg_metrics[2] /= batch.num
        if not suppress_output :
            print ('%5d  ') % (r+1),
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

