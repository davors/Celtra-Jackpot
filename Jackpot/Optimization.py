from Config import *
from MABsolver import *
from Evaluator import *

class Optimizer() :
    
    MABsolver = None                #multi-armed-bandit policy
    fitnessMetric = None            #choosen fitness metric
    selectiveOptimization = None    #choosen parameters to optimize - array of indices
    optimizationAlgorithm = None    #choosen optimization algorithm
    optimizationConfig = None       #array of parameters for the optimization algorithm
    evaluationsPerStep = None       #number of evaluations per each parameter sample

    def __init__(
        self, 
        MABsolver,
        evaluationsPerStep = DEFAULT_OPTIMIZATION_EVALS_PER_SAMPLE,
        selectiveOptimization = None,
        optimizationConfig = DEFAULT_OPTIMIZATION_CONFIG,
        fitnessMetric = DEFAULT_FITNESS_METRIC,
        optimizationAlgorithm = DEFAULT_OPTIMIZATION_ALGORITHM,
        ) :

        self.MABsolver = MABsolver
        self.fitnessMetric = fitnessMetric
        self.optimizationAlgorithm = optimizationAlgorithm
        self.optimizationConfig = optimizationConfig
        self.evaluationsPerStep = evaluationsPerStep
        
        if selectiveOptimization is None :
            self.selectiveOptimization = range(len(self.MABsolver.config.params))
        else :
            self.selectiveOptimization = selectiveOptimization


    def Optimize(
        self,
        batch,                  #test cases
        startingValues = None,  #optimized parameters starting values
        suppress_output = 0
        ) :
        
        #get list of parameters from MAB solver
        paramValues = self.MABsolver.listParams(self.selectiveOptimization)
        numParams = len(paramValues)

        #set searched parameters to specified initial values
        if not (startingValues is None) :
            paramValues = startingValues
            self.MABsolver.setParams(paramValues, self.selectiveOptimization)

        #user output
        if not suppress_output :
            print 'Procedure Optimizer.Optimize()'
            self.info()
            self.MABsolver.config.info()
            batch.info()

        #optimization algorithms
        if self.optimizationAlgorithm == GLODEF_OPTIMIZATION_ANNEALING :
        
            #for some iterative procedure
            for i in range(10) :
                
                #evaluate new (or all) samples
                score = evaluateBatch(self.MABsolver, batch, self.evaluationsPerStep, 1 )[0][self.fitnessMetric]
                
                if not suppress_output :
                    print '%2d   %.1f   ' % (i+1, score),
                    print '%s' % ', '.join(map(str, paramValues))

                #do something with parameters -> create new sample
                paramValues[0] += 0.2
                self.MABsolver.setParams(paramValues, self.selectiveOptimization)

            #out of for loop
            #print best_sample_score and param setting
            #set best parameter values
            #self.MABsolver.setParams(paramValues, self.selectiveOptimization)

        elif self.optimizationAlgorithm == GLODEF_OPTIMIZATION_GENETIC :
            todo

        #return best sample and its score
        #return (best_sample, best_score)
        #TODO
        
    #optimize on a learning batch and evaluate on another batch
    def OptimizeEvaluate(
        self,
        learnBatch,
        evalBatch,
        evalRepeats,
        suppress_output = 0
        ) :
    
        self.Optimize(learnBatch, suppress_output)
        evaluateBatch(self.MABsolver, evalBatch, evalRepeats, suppress_output)

    def CrossOptimizeEvaluate() :
        todo

    def info(self):
        print 'Optimizer(): %s , %s' % (
            GLO_labels_optimization[self.optimizationAlgorithm], 
            GLO_labels_metrics[self.fitnessMetric], 
            )

        print 'Optimizer(): config: ',
        for i in range(len(self.optimizationConfig)) :
            print '%f ' % self.optimizationConfig[i],
        print ''
        print 'Optimizer(): selective: ',
        for i in range(len(self.selectiveOptimization)) :
            print '%f ' % self.selectiveOptimization[i],
        print ''
        print 'Optimizer(): evals/step: %d' % self.evaluationsPerStep