from Config import *
from MABsolver import *
from BanditGenerator import *

def evaluateSingleCase(
    solver,                 # the MABsolver object (it incorporates algorithms for solving the non-stohastic multi-armed bandit problem)
    case,                   # a multi-armed bandit problem
    suppress_output = 0,    # enable/disable print output
    oracleProbablity = 0    # gather bandits probability instead of -> can only be used on BanditGenerator() classes, so NOT on ONLINE (url) scenarios
    ) :

    #init solver
    solver.resetState(case.numBandits)

    #init stats
    total_reward = 0.0

    #compute single case evaluation
    for p in xrange(case.maxPulls) :

        #TODO PARAM_INPUTS if not direct parameter search (if linear or neural used...), update inputs in function approximator for parameters
        #example:
        # solver.config.params[0].updateInputs( array_of_new_inputs )
        #or
        # solver.config.params[0].lastInputs[0] = some_new_input1
        # solver.config.params[0].lastInputs[1] = some_new_input2
        # solver.config.params[1].lastInputs[0] = some_new_input1
        # solver.config.params[1].lastInputs10] = some_new_input2
        # solver.config.params[2].lastInputs[0] = some_new_input3

        selected_bandit = solver.selectBandit()         #apply selection policy

        #get reward
        if(oracleProbablity == 0) :
            reward = case.pullBandit(selected_bandit, p)    # returns value 0 or 1
        else :
            reward = case.probBandit(selected_bandit, p)    # returns probability in the interval [0 , 1]

        #TODO PARAM_INPUTS (same as above)

        solver.update(selected_bandit, reward, 1)     #update solver stats
        total_reward += reward                          #sum of collected reward

    #output stats
    if not suppress_output:
        solver.infoStats()
        print 'Total reward: '+str(total_reward)+' maximum possible reward: '+str(case.maximumReward)

    return total_reward

def evaluateBatch(
    solver,                 # the MABsolver object (it incorporates algorithms for solving the non-stohastic multi-armed bandit problem)
    batch,                  # batch of testing scenarios
    repeats,                # number of evaluative repeats
    suppress_output = 0,    # enable/disable print output
    oracleProbablity = 0    # if enabled (1): gather bandits probability instead of -> can only be used on BanditGenerator() classes, so NOT on ONLINE (url) scenarios
    ) :

    #init performance metrics
    num_metrics = DEFAULT_EVAL_NUM_METRICS
        #0 - sum of rewards
        #1 - regret
        #2 - optimality factor (sum of rewards divided by maximum possible reward) in %
        #3 - Random-normalized optimality in %

    metrics = [[0.0 for x in xrange(batch.num)] for x in xrange(num_metrics)]
    avg_metrics = [0.0 for x in xrange(num_metrics)]
    new_avg_metrics = [0.0 for x in xrange(num_metrics)]
    new_metrics = [0.0 for x in xrange(num_metrics)]

    #user output
    if not suppress_output :
        print 'Procedure evaluateBatch()'
        if oracleProbablity == 0 :
            print 'Oracle probabilites : disabled'
        else :
            print '!!! --- WARNING --- !!! Oracle probabilites : ENABLED !!! --- WARNING --- !!!'
        solver.config.info()
        batch.info()
        print 'Total repeats: %d' %repeats
        print ''
        print '           Batch performances                           ',
        print 'By-cases performance as: %s' % GLO_labels_metrics[DEFAULT_FITNESS_METRIC]
        print ''
        print 'repeat ',
        for i in xrange(num_metrics):
            print '%s' % GLO_shortLabels_metrics[i],
        print '     ',
        for c in xrange(batch.num) :
            print '   case%02d' % (c+1),
        print ''
        print ''

    #evaluate all cases
    for r in xrange(repeats) :

        #reset averaged (through cases) metrics
        for i in xrange(num_metrics):
            new_avg_metrics[i] = 0.0
        
        for c in xrange(0,batch.num) :
            #execute bandit game (case)
            new_result = evaluateSingleCase(solver, batch.list[c], 1, oracleProbablity)

            #-- DEFINE HERE CUSTOM METRICS --#
            new_metrics[0] = new_result
            new_metrics[1] = (batch.list[c].maximumReward - new_result)
            new_metrics[2] = new_result / batch.list[c].maximumReward * 100.0
            new_metrics[3] = (new_result - batch.list[c].randomReward) / (batch.list[c].maximumReward - batch.list[c].randomReward) * 100.0

            #update results by different metrics
            for i in xrange(num_metrics):
                metrics[i][c] +=  (1.0/(r+1.0))*(new_metrics[i] - metrics[i][c])
                new_avg_metrics[i] += new_metrics[i]

        #calculate overall performance
        new_avg_metrics[2] /= batch.num
        new_avg_metrics[3] /= batch.num
        for i in xrange(num_metrics):
            avg_metrics[i]  += (1.0/(r+1.0))*(new_avg_metrics[i] - avg_metrics[i])

        #user ouput
        if not suppress_output :
            print ('%6d ') % (r+1),
            for i in xrange(num_metrics):
                print (GLO_metrics_out_format[i]) % (avg_metrics[i]),
            print '     ',
            for c in xrange(batch.num) :
                print (GLO_metrics_out_format[DEFAULT_FITNESS_METRIC]) % metrics[DEFAULT_FITNESS_METRIC][c],
            print ''

    if not suppress_output :
        print ''
        print 'Procedure evaluateBatch(): COMPLETED'
        print ''

    #returns
    #   measurements averaged over all cases
    #   measurements for each case individually
    return (avg_metrics, metrics)

