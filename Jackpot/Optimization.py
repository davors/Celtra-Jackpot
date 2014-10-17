from Config import *
from MABsolver import *
from Evaluator import *

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
            print 'Optimizer(): numParams: %d' % numParams
            self.MABsolver.config.info()
            batch.info()
            print ''

        #-- optimization algorithms --#
        if self.optimizationAlgorithm == GLODEF_OPTIMIZATION_ANNEALING :
        
            #for some iterative procedure
            for i in range(10) :
                
                #evaluate new (or all) samples
                score = evaluateBatch(self.MABsolver, batch, self.evaluationsPerSample, 1, oracleProbablity)[0][self.fitnessMetric]
                if not suppress_output :
                    print '%2d   %.1f   ' % (i+1, score),
                    print '%s' % ' '.join(map(str, paramValues))

                #do something with parameters -> create new sample
                paramValues[0] += 0.2
                self.MABsolver.setParams(paramValues, self.selectiveOptimization)

            #out of for loop
            #print best_sample_score and param setting
            #set best parameter values
            #self.MABsolver.setParams(paramValues, self.selectiveOptimization)

        elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_GENETIC :
            todo

        elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_GENETIC :
            todo

        elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_EXHAUSTIVE :
            #recursive exhaustive search
            self.exhaustiveSearch(batch, paramValues, suppress_output, oracleProbablity, 0)

        if not suppress_output :
            print ''
            print 'Procedure Optimizer.Optimize(): COMPLETED'
            print ''

        #return best sample and its score
        #return (best_sample, best_score)
        #TODO
        
    #optimize on a learning batch and evaluate on another batch
    def OptimizeEvaluate(
        self,
        learnBatch,
        evalBatch,
        evalRepeats,
        optimizationConfig = None,  # array of parameters for the optimization algorithm
        suppress_output = 0,        # enable/disable print output
        oracleProbablity = 0        # if enabled (1): gather bandits probability instead of -> can only be used on BanditGenerator() classes, so NOT on ONLINE (url) scenarios
        ) :
    
        if not suppress_output :
            print 'Procedure Optimizer.OptimizeEvaluate()'
        
        self.Optimize(learnBatch, optimizationConfig, suppress_output, oracleProbablity)
        evaluateBatch(self.MABsolver, evalBatch, evalRepeats, suppress_output, oracleProbablity)
        
        if not suppress_output :
            print ''
            print 'Procedure Optimizer.OptimizeEvaluate(): COMPLETED'
            print ''

    def CrossOptimizeEvaluate() :
        todo

    def info(self):
        print 'Optimizer(): %s , %s' % (
            GLO_labels_optimization[self.optimizationAlgorithm], 
            GLO_labels_metrics[self.fitnessMetric], 
            )

        print 'Optimizer(): config: ',
        PrintStrings(self.optimizationConfig)
        print 'Optimizer(): selective: ',
        for i in range(len(self.selectiveOptimization)) :
            print '%f ' % self.selectiveOptimization[i],
        print ''
        print 'Optimizer(): evals/step: %d' % self.evaluationsPerSample

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