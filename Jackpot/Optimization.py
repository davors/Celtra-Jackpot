from configuration import *
from evaluation import *

#TODO - IMPLEMENT SOME OPTIMIZATION PROCEDURE

def Optimize(
    cases,
    optimization_algorithm,
    optimization_algorithm_params,
    evaluations_per_sample,
    fitness_metric,
    strategy_settings,
    function_approximator,
    suppress_output = 0
    ) :

    num_parameters = function_approximator.num_params


    if not suppress_output :
        print 'Procedure Optimize()'
        print 'Settings: %s , %s , params: ' % (GLO_labels_optimization[optimization_algorithm], GLO_labels_metrics),
        for i in xrange(len(optimization_algorithm_params)) :
            print '%f' % optimization_algorithm_params[i],
        print ''
        print 'Eval per sample: %d' % evaluations_per_sample
        print 'Strategy Settings: %s , %s , %s' % (GLO_labels_selection_policies[strategy_settings[0]], GLO_labels_change_point_detectors[strategy_settings[1]], GLO_labels_reset_algorithms[strategy_settings[2]])
        print 'Function approximator: %s' % GLO_labels_function_approx[function_approximator]
        print 'Strategy param values %f %f %f %f' % (strategy_settings[0], strategy_settings[1], strategy_settings[2], strategy_settings[3])
        print 'Case list: ',
        for i in xrange(num_cases) :
            print '%d ' % cases[i].ID,
        print ''
        print 'Total cases: ' + str(num_cases)

    if optimization_algorithm == GLODEF_OPTIMIZATION_ANNEALING :
        
        #for some iterative procedure
            #do something with parameters -> create new sample
            #evaluate new (or all) samples

            single_sample_score = evaluation_batch_cases(cases, evaluations_per_sample, 1, strategy_settings, [DEFAULT_PAR_EGREEDY_E, DEFAULT_PAR_SOFTMAX_T, DEFAULT_PAR_UCB1_C, DEFAULT_PAR_CHANGEPOINT_THR], function_approximator)[0][fitness_metric]

            #print best_sample_score and param setting

    elif optimization_algorithm == GLODEF_OPTIMIZATION_GENETIC :
        todo

    #return best sample and its score
    #return (best_sample, best_score)

