from __future__ import division
from Config import *
from MABsolver import *
from Evaluator import *
import random
import math
import sys

class Optimizer() :

    MABsolver = None                #multi-armed-bandit policy
    fitnessMetric = None            #choosen fitness metric
    optimizationAlgorithm = None    #choosen optimization algorithm
    optimizationConfig = None       #array of parameters for the optimization algorithm
    evaluationsPerSample = None     #number of evaluations per each parameter sample
    selectiveOptimization = None    #choosen parameters to optimize - array of indices

    def __init__(
        self,
        MABsolver,
        evaluationsPerSample = DEFAULT_OPTIMIZATION_EVALS_PER_SAMPLE,
        optimizationConfig = DEFAULT_OPTIMIZATION_CONFIG,
        fitnessMetric = DEFAULT_FITNESS_METRIC,
        optimizationAlgorithm = DEFAULT_OPTIMIZATION_ALGORITHM,
        selectiveOptimization = None
        ) :

        self.MABsolver = MABsolver
        self.fitnessMetric = fitnessMetric
        self.optimizationAlgorithm = optimizationAlgorithm
        self.optimizationConfig = optimizationConfig
        self.evaluationsPerSample = evaluationsPerSample

        if selectiveOptimization is None :
            self.selectiveOptimization = range(len(self.MABsolver.config.params))
        else :
            self.selectiveOptimization = selectiveOptimization


    def Optimize(
        self,
        batch,                          # test cases
        optimizationConfig = None,      # array of parameters for the optimization algorithm
        completeRepeats = 1,            # number of repeats of whole optimization procedure (to start multiple times from initial point - good if optimization algorithm tedns to get stuck in a local maximum)
        suppress_output = 0,            # enable/disable print output
        oracleProbablity = 0            # if enabled (1): gather bandits probability instead of -> can only be used on BanditGenerator() classes, so NOT on ONLINE (url) scenarios
        ) :

        #get list of parameters from MAB solver
        paramValues = self.MABsolver.listParams(self.selectiveOptimization)
        numParams = len(paramValues)

        #set searched parameters to specified initial values
        if not (optimizationConfig is None) :
            self.optimizationConfig = optimizationConfig

        #user output
        if not suppress_output :
            print 'Procedure Optimizer.Optimize()'
            if oracleProbablity == 0 :
                print 'Oracle probabilites : disabled'
            else :
                print '!!! --- WARNING --- !!! Oracle probabilites : ENABLED !!! --- WARNING --- !!!'
            self.info()
            print 'Optimizer(): numParams: %d , completeRepeats: %d' % (numParams, completeRepeats)
            self.MABsolver.config.info()
            batch.info()
            print ''

        #-- optimization algorithms --#
        best_sample = None
        best_score = None

        # multiple repeats of an optimization run
        for r in range(completeRepeats) :

            if self.optimizationAlgorithm == GLODEF_OPTIMIZATION_ANNEALING :
                (last_sample, last_score) = self.simulatedAnnealing(batch, paramValues, suppress_output, oracleProbablity)

            elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_GENETIC :
                todo

            elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_GENETIC :
                todo

            elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_EXHAUSTIVE :
                #recursive exhaustive search
                (last_sample, last_score) = self.exhaustiveSearch(batch, paramValues, suppress_output, oracleProbablity, 0)

            # remember best
            if( last_score > best_score ) :
                best_score = last_score
                best_sample = last_sample


        #if not suppress_output :
        #    print ''
        #    print 'Procedure Optimizer.Optimize(): COMPLETED'
        #    print ''

        #return best sample and its score
        return (best_sample, best_score)

    #optimize on a learning batch and evaluate on another batch
    def OptimizeEvaluate(
        self,
        learnBatch,
        evalBatch,
        evalRepeats,
        optimizationConfig = None,  # array of parameters for the optimization algorithm
        completeRepeats = 1,        # number of repeats of whole optimization procedure (to start multiple times from initial point - good if optimization algorithm tedns to get stuck in a local maximum)
        suppress_output = 0,        # enable/disable print output
        oracleProbablity = 0        # if enabled (1): gather bandits probability instead of -> can only be used on BanditGenerator() classes, so NOT on ONLINE (url) scenarios
        ) :

        if not suppress_output :
            print 'Procedure Optimizer.OptimizeEvaluate()'

        (best_sample, best_score) = self.Optimize(learnBatch, optimizationConfig, completeRepeats, suppress_output, oracleProbablity)
        self.MABsolver.setParams(best_sample, self.selectiveOptimization)
        evaluateBatch(self.MABsolver, evalBatch, evalRepeats, suppress_output, oracleProbablity)

        #if not suppress_output :
        #    print ''
        #    print 'Procedure Optimizer.OptimizeEvaluate(): COMPLETED'
        #    print ''

    def CrossOptimizeEvaluate() :
        todo

    def info(self):
        print 'Optimizer(): %s , %s' % (
            GLO_labels_optimization[self.optimizationAlgorithm],
            GLO_labels_metrics[self.fitnessMetric],
            )

        print 'Optimizer(): config: ',
        PrintStrings(self.optimizationConfig)
        print 'Optimizer(): selective: [ ',
        for i in range(len(self.selectiveOptimization)) :
            print '%d ' % self.selectiveOptimization[i],
        print ']'
        print 'Optimizer(): evals/step: %d' % self.evaluationsPerSample

    #recursive exhaustive search of complete discretized parameter space
    def exhaustiveSearch(self, batch, paramValues, suppress_output, oracleProbablity, level) :

        bestScore = -1e30000
        bestParams = None
        paramValues[level] = self.optimizationConfig[level][0]      #set initial values
        for i in xrange(self.optimizationConfig[level][2]) :        #for iterate number of steps

            if(level == (len(paramValues)-1) ) :
                self.MABsolver.setParams(paramValues, self.selectiveOptimization)
                score = evaluateBatch(self.MABsolver, batch, self.evaluationsPerSample, 1, oracleProbablity)[0][self.fitnessMetric]
                params = paramValues
                if not suppress_output :
                    print GLO_metrics_out_format[self.fitnessMetric] % score,
                    print '  ',
                    for p in xrange(len(paramValues)) :
                        print ' %f' % paramValues[p],
                    print ''

            else :
                (score, params) = self.exhaustiveSearch(batch, paramValues, suppress_output, oracleProbablity, level + 1)

            if(score >= bestScore) :
                bestScore = score
                bestParams = params

            paramValues[level] += self.optimizationConfig[level][1]        #increase parameter value by step rate

        return (bestScore, bestParams)


    #simulated annealing search algorithm
    def simulatedAnnealing(self, batch, paramValues, suppress_output, oracleProbablity):

        # CONFIGURATION
        BOUND_LOWER = self.optimizationConfig[0]
        BOUND_UPPER = self.optimizationConfig[1]
        GRID_STEP   = self.optimizationConfig[2] # Leave empty for unconstraint search (continuous)
        START_VALUES = paramValues;              # leave empty for random initialization
        NUM_CYCLES  = self.optimizationConfig[3] # number of cycles (epochs) of SA
        NUM_TRIALS_PER_CYCLE = self.optimizationConfig[4] # number of iterations per each cycle
        P_START = self.optimizationConfig[5] # Probability of accepting worse solution at the start
        P_END = self.optimizationConfig[6] # Probability of accepting worse solution at the end
        NEIGH_RADIUS_START = self.optimizationConfig[7]
        NEIGH_RADIUS_END = self.optimizationConfig[8]
                           # when choosing next candidate, search only the neighbourhood
                           # of current solution. NEIGH_RADIUS is a ratio of full interval
                           # span, i.e.: NEIGH_RADIUS * (BOUND_UPPER - BOUND_LOWER)

        # define objective function
        def f(paramValues):

            self.MABsolver.setParams(paramValues, self.selectiveOptimization)
            score = evaluateBatch(self.MABsolver, batch, self.evaluationsPerSample, 1, oracleProbablity)[0][self.fitnessMetric]

            if not suppress_output :
                print GLO_metrics_out_format[self.fitnessMetric] % score,
                print '  ',
                for p in xrange(len(paramValues)) :
                    print ' %f' % paramValues[p],
                print ''
                sys.stdout.flush()

            return score

        # define function that returns new trial point (solution candidate)
        def get_new_candidate(x_curr,neigh_radius):
            if not neigh_radius:
                neigh_radius = 1.0

            x = [0 for i in xrange(num_params)]
            for i in xrange(num_params):

                if not x_curr:
                    # choose a random point from whole interval
                    lowEnd = BOUND_LOWER[i]
                    highEnd = BOUND_UPPER[i]

                else:
                    x_curr_i = x_curr[i]
                    r = neigh_radius * abs(BOUND_UPPER[i]-BOUND_LOWER[i])*0.5
                    lowEnd = max(x_curr_i - r, BOUND_LOWER[i])
                    highEnd = min(x_curr_i + r, BOUND_UPPER[i])

                x[i] = random.uniform(lowEnd,highEnd)

                if GRID_MODE == "discrete":
                    # Compute point in the grid
                    remainder = x[i] % GRID_STEP[i]
                    quocient = x[i] // GRID_STEP[i]
                    if remainder >= (0.5*GRID_STEP[i]):
                        x[i] = (quocient+1)*GRID_STEP[i]
                    else:
                        x[i] = quocient*GRID_STEP[i]

            return x

##        def linspace(start, stop, step):
##            n = int(math.ceil(((stop - start) / step)) +1)
##            v = [0 for i in xrange(n)]
##
##            for i in range(n):
##                v[i]=(start + step * i)
##            return v


        ################################################################################
        # Checks
        num_params = len(BOUND_LOWER)
        if num_params != len(BOUND_UPPER):
            print("Length of BOUND_UPPER does not match with others!\n")

        GRID_MODE = "continuous"
        if GRID_STEP:
            GRID_MODE = "discrete"
            if (num_params != len(GRID_STEP)):
                print("Length of GRID_STEP does not match with others! Switching to continuous mode.\n")
                GRID_MODE = "continuous"

        # Start values - random if empty
        if not START_VALUES:
            x_start = get_new_candidate(None,None)
        else:
            if num_params != len(START_VALUES):
                print("Length of START_VALUES does not match with others!\n")
            else:
                x_start = START_VALUES


        ##################################################
        # Simulated Annealing
        ##################################################
        # Number of accepted solutions
        num_accepted = 0.0

        # Initial temperature
        t_start = -1.0/math.log(P_START)

        # Final temperature
        t_end = -1.0/math.log(P_END)

        # Fractional reduction every cycle
        frac = (t_end/t_start)**(1.0/(NUM_CYCLES-1.0))

        # Initialize x
        x = [[0 for i in xrange(num_params)] for j in xrange(NUM_CYCLES+1)]
        x[0] = x_start

        # current trial points
        xi = x_start
        num_accepted = num_accepted + 1.0

        # Current best results so far
        xc = x[0]
        fc = f(xi)
        fs = [0 for i in xrange(NUM_CYCLES+1)]
        fs[0] = fc

        # Current temperature
        t = t_start

        # Current neighbourhood radius
        neigh_radius = NEIGH_RADIUS_START
        neigh_radius_delta = (NEIGH_RADIUS_START-NEIGH_RADIUS_END)/(NUM_CYCLES-1)

        # DeltaE Average
        DeltaE_avg = 0.0

        for i in range(NUM_CYCLES):
            #if not suppress_output :
            print 'Cycle: ' + str(i) + ', Temperature: ' + str(t) + ', neigh_radius: ' +str(neigh_radius) + ', score: ' + str(fc)

            for j in range(NUM_TRIALS_PER_CYCLE):
                # Generate new trial points
                xi = get_new_candidate(xc,neigh_radius)
                objFuncVal = f(xi)

                DeltaE = abs(objFuncVal-fc)
                if (objFuncVal < fc):
                    # Initialize DeltaE_avg if a worse solution was found
                    #   on the first iteration
                    if (i==0 and j==0): DeltaE_avg = DeltaE
                    # objective function is worse
                    # generate probability of acceptance
                    p = math.exp(-DeltaE/(DeltaE_avg * t))
                    # determine whether to accept worse point
                    if (random.random()<p):
                        # accept the worse solution
                        accept = True
                    else:
                        # don't accept the worse solution
                        accept = False
                else:
                    # objective function is lower, automatically accept
                    accept = True
                if (accept==True):
                    # update currently accepted solution

                    for kk in range(len(xi)):
                        xc[kk] = xi[kk]

                    fc = objFuncVal
                    # increment number of accepted solutions
                    num_accepted = num_accepted + 1.0
                    # update DeltaE_avg
                    DeltaE_avg = (DeltaE_avg * (num_accepted-1.0) +  DeltaE) / num_accepted
            # Record the best x values at the end of every cycle
            for kk in range(len(xc)):
                x[i+1][kk] = xc[kk]
            fs[i+1] = fc
            # Lower the temperature for next cycle
            t = frac * t
            # Tighten neighbourhood for next cycle
            neigh_radius = neigh_radius - neigh_radius_delta


        ## print solution
        #if not suppress_output :
        #    print 'Optimization with Simulated Annealing is over.'
        #    print 'Best solution: ' + str(xc)
        #    print 'Best score: ' + str(fc)

        return (xc, fc)
