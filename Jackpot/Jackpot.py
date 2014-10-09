import configuration
from changePointDetection import *
from fileIO import *
from SampleAnalyzer import *
from machine import *
from strategy import *
from BanditGenerator import *

#for c in range(1,configuration.N_CASES+1):
#    machines=getNumMachines(c)
#    pulls=getNumPulls(c)
#    reps=1   
#    #if c<=5: 
#    #    reps=20000/pulls
#    #else: 
#    #    reps=20000
#    if configuration.TEST==1:
#        writeDataToFile(c,machines,pulls,reps)
#(case, machines, pulls, reps, data)=loadDataFromFile('case_06_02m_01000p.txt')
#M=[machine(m+1) for m in range(machines)]

#pulls=1000
#for i in range(0,500):
#    data[0][i]=int(random.random()<0.6)
#    data[1][i]=int(random.random()<0.4)

#for i in range(500,1000):
#    data[0][i]=int(random.random()<0.4)
#    data[1][i]=int(random.random()<0.6)

def evaluation_artificial_cases(case_list, repeats) :

    #defines
    num_metrics = 1

    #init
    num_cases = len(case_list)

    cases = [BanditTestCase() for count in xrange(configuration.N_CASES)]

    case=0

    cases[case].numBandits = 2
    cases[case].maxPulls = 1000
    cases[case].bandits = [BanditGenerator() for count in xrange(cases[case].numBandits)]
    cases[case].bandits[0].intervals = [0,500]
    cases[case].bandits[1].intervals = [0,500]
    cases[case].bandits[0].probabilities = [0.5,0.1]
    cases[case].bandits[1].probabilities = [0.1,0.5]

    #compute maximal possible sum of rewards
    summedMaxRewards = 0.0
    for c in xrange(0,num_cases) :
        summedMaxRewards += cases[c].calcMaxReward()

    #user output
    print 'Procedure evaluation_artificial_cases()'
    #print 'Case list: ' + case_list
    print 'Total cases: ' + str(num_cases)
    print 'Maximum summed reward: ' + str(summedMaxRewards)
    print 'Repeats: ' + str(repeats)
    
    #init stats
    avg_results = [0.0 for x in xrange(num_cases)]
    avg_sum_results = 0.0

    #evaluate all cases
    for r in xrange(repeats) :
        last_avg_results = 0
        for c in xrange(0,num_cases) :
            last_result = single_case_evaluation(cases[case], 0)

            #store results
            avg_results[c] += (1.0/(r+1.0))*(last_result - avg_results[c])
            last_avg_results += last_result
                    
        #calculate overall performance
        last_avg_results /= num_cases
        avg_sum_results  += (1.0/(r+1.0))*(last_avg_results - avg_sum_results)

        print("%0.2f" % avg_sum_results)
        

def single_case_evaluation(case, print_output = 1) :      
    
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
    total_reward = 0
    for m in machines:
        total_reward = total_reward + m.sum_total
        if print_output :
            print 'Machine '+str(m.id)+' Total reward: '+str(m.sum_total)+' Total pulls: '+str(m.pulls_total)+' Average reward: '+str(m.mean)

    if print_output:
        print 'Total reward: '+str(totalReward)+' maximum possible reward: '+str(maxReward)

    return total_reward


evaluation_artificial_cases([0], 100)


#Y=[]
#X=0
#m=2
#Y2=0
#HP=0
#mt=0
#Mt=0
#for i in range(1,pulls+1):
#    X=X+data[m-2][i-1]
#    (s,A,Y)=checkChange(2.5,X, Y, i, data[m-2][0:i])
#    #(s,A,Y)=checkChange(1.96,X, Y, i, data[m-2][0:i])
#    if(s>0):
#        print 'checkChange triggered at: '+str((s,A,Y,i))
#        break
    #(status, HP, Mt, Y2)=HankeyPankeyTest(80,HP, Mt,data[m-2][i-1], Y2, i)
    #if(status==1):
    #    print 'HankeyPankey triggered at: '+str((HP,i))
    #    break

#print str(case)    





### TOM ###

#testcases = [BanditTestCase() for count in xrange(configuration.N_CASES)]

#testcases[0].numBandits = 2
#testcases[0].maxPulls = 500
#testcases[0].bandits = [BanditGenerator() for count in xrange(testcases[0].numBandits)]
#testcases[0].bandits[0].intervals = [0,250]
#testcases[0].bandits[1].intervals = [0,250]
#testcases[0].bandits[0].probabilities = [0.1,0.5]
#testcases[0].bandits[1].probabilities = [0.5,0.4]
#maxR = testcases[0].calcMaxReward()

#SampleAnalyzer('case_06_02m_01000p_1000r.txt')
#SampleAnalyzer('case_06_02m_01000p_1000r.txt')