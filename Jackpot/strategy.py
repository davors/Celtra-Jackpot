#Different strategies for tackling the problem
from Config import *
import random
from math import *

#the UCB algorithm by Auer et al., 2002
def UCB1(actions, all_pulls, parC = 1.0):
    
    bestVal = -1e30000
    numEqualBest = 1
    indicesBest = [-1]*len(actions)

    #find best action among all available
    for i in range(len(actions)) :

        a = actions[i]

        #first try all the unexplored actions (those with zero visits)
        if a.pulls <= 0 :
            indicesBest[0] = i
            break

        #if all actions already explored, calculate their values
        else :
            UCBvalue = a.mean + parC*sqrt(2.0*log(all_pulls)/a.pulls)   #the UCB1 equation

            #store calculated value
            a.storedValue = UCBvalue

            #find action with highest value
            if UCBvalue > bestVal :
                bestVal = UCBvalue
                numEqualBest = 1
                indicesBest[numEqualBest-1] = i

            #remember best
            elif UCBvalue == bestVal :
                numEqualBest += 1
                indicesBest[numEqualBest-1] = i

    #break ties randomly
    indicesBest[0] = indicesBest[random.randint(0,numEqualBest-1)]

    return actions[indicesBest[0]]


def UCBT(actions, all_pulls, parC = 1.0):
    
    bestVal = -1e30000
    numEqualBest = 1
    indicesBest = [-1]*len(actions)

    #find best action among all available
    for i in range(len(actions)) :

        a = actions[i]

        #first try all the unexplored actions (those with zero visits)
        if a.pulls <= 0 :
            indicesBest[0] = i
            break

        #if all actions already explored, calculate their values
        else :
            try:
                #UCBvalue = a.mean + parC*sqrt(2.0*log(all_pulls)/a.pulls)   #the UCB1 equation
                V = a.variance+sqrt(2.0*log(all_pulls)/a.pulls)
                UCBvalue = a.mean + parC * sqrt((log(all_pulls)/a.pulls)*min(1.0/4.0,V))

                #store calculated value
                a.storedValue = UCBvalue

                #find action with highest value
                if UCBvalue > bestVal :
                    bestVal = UCBvalue
                    numEqualBest = 1
                    indicesBest[numEqualBest-1] = i

                #remember best
                elif UCBvalue == bestVal :
                    numEqualBest += 1
                    indicesBest[numEqualBest-1] = i

            except:
                print 'UCBT(): lol'

    #break ties randomly
    indicesBest[0] = indicesBest[random.randint(0,numEqualBest-1)]

    return actions[indicesBest[0]]


def SoftMax(M, tao):

    # hardcoded limitation due to numerical stability
    if tao > 0.001 :

        #average = 0.0
        #variance = 0.0

        #meanT = [0.0] * len(M)
        #for m in xrange(len(M)) :
        #    meanT[m] = (M[m].mean) 
        #    old_avg = average
        #    average = average + (meanT[m] - average) / (m + 1)
        #    variance = variance + (meanT[m] - average) * (meanT[m] - old_avg)

        #deviation = sqrt(variance/len(M))
        
        #if deviation == 0.0 :
        #    values = [m.mean for m in M]
        #    return M[CompleteGreedy(values)]
        #Norm=[ (1.0 / (1.0 + exp(-(m-average)/deviation) ) ) for m in meanT]
        #E=[exp(a) for a in Norm]

        A=[m.mean for m in M]
        E=[exp(a/tao) for a in A]
        E_sum=sum(E)
        P=[e/E_sum for e in E]

        sp = 0.0
        rpoint = random.random()
        for i in xrange(len(P)):
            sp = sp + P[i]
            if rpoint < sp:
               return (M[i])

    # if temperature is close to zero, then the algorithm is pratically completely greedy
    else :
        values = [m.mean for m in M]
        return M[CompleteGreedy(values)]

def CompleteGreedy(valueList) :
    bestVal = -1e30000
    numEqualBest = 1
    indicesBest = [-1]*len(valueList)
    for i in xrange(len(valueList)) :

        #find action with highest value
        if valueList[i] > bestVal :
            bestVal = valueList[i]
            numEqualBest = 1
            indicesBest[numEqualBest-1] = i

        #remember best
        elif valueList[i] == bestVal :
            numEqualBest += 1
            indicesBest[numEqualBest-1] = i

    #break ties randomly
    indicesBest[0] = indicesBest[random.randint(0,numEqualBest-1)]

    return indicesBest[0]

def EGreedy(M, E):
    Avg=[m.mean for m in M]
    maxM=Avg.index(max(Avg))
    P=[float(E)/len(M)]*len(M)
    P[maxM]=1-E+E/len(M)
    sp = 0.0
    rpoint = random.random()
    for i in xrange(len(P)):
        sp = sp + P[i]
        if rpoint < sp:
            return (M[i])
