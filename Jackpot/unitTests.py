from Config import *
from fileIO import *
from SampleAnalyzer import *
from Jackpot_init import *
from MABsolver import *
from Evaluator import *
from Optimization import *
from unitTests import *

def unitTest_Optimizer(allCases) :
    testBatch_tmp = BanditTestBatch( allCases, [10] )
    testSolver = MABsolver([1.0],)
    optimizer = Optimizer(testSolver,50,[],[0],GLODEF_FITNESS_OPTIMALITY,GLODEF_SELECTION_UCB1)
    optimizer.Optimize(testBatch_tmp, [0.0])
    optimizer.OptimizeEvaluate()