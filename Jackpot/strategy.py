#Different strategies for tackling the problem
from Config import *
import random
from math import *

#the UCB algorithm by Auer et al., 2002
def UCB1(actions, all_pulls, parC = 1.0):
    
    selectedAction = None
    bestVal = -1e30000

    #find best action among all available
    for a in actions :

        #first try all the unexplored actions (those with zero visits)
        if a.pulls <= 0 :
            selectedAction = a
            break

        #if all actions already explored, calculate their values
        else :
            UCBvalue = a.mean + parC*sqrt(2.0*log(all_pulls)/a.pulls)   #the UCB1 equation

            #find action with highest value
            if UCBvalue >= bestVal :
                bestVal = UCBvalue
                selectedAction = a

            #break ties sequentially randomly
            elif UCBvalue == bestVal :
                if not (selectedAction is None) :
                    if random.random() < 0.5 :
                        selectedAction = a
                else :
                    selectedAction = a

    return selectedAction


def UCBT(actions, all_pulls, parC = 1.0):
    
    selectedAction = None
    bestVal = -1e30000

    #find best action among all available
    for a in actions :

        #first try all the unexplored actions (those with zero visits)
        if a.pulls <= 0 :
            selectedAction = a
            break

        #if all actions already explored, calculate their values
        else :
            #UCBvalue = a.mean + parC*sqrt(2.0*log(all_pulls)/a.pulls)   #the UCB1 equation
            V = a.variance+sqrt(2.0*log(all_pulls)/a.pulls)
            UCBvalue = a.mean + parC * sqrt((log(all_pulls)/a.pulls)*min(1.0/4.0,V))
            #find action with highest value
            if UCBvalue >= bestVal :
                bestVal = UCBvalue
                selectedAction = a

            #break ties sequentially randomly
            elif UCBvalue == bestVal :
                if not (selectedAction is None) :
                    if random.random() < 0.5 :
                        selectedAction = a
                else :
                    selectedAction = a

    return selectedAction
    return 0


def SoftMax(M, tao):
    Avg=[m.mean for m in M]
    E=[exp(a/tao) for a in Avg]
    E_sum=sum(E)
    P=[e/E_sum for e in E]


    sp=0;
    for i in range(0,len(P)):
        sp=sp+P[i]
        if random.random()<sp:
           return (M[i])


def EGreedy(M, E):
    Avg=[m.mean for m in M]
    maxM=Avg.index(max(Avg))
    P=[float(E)/len(M)]*len(M)
    P[maxM]=1-E+E/len(M)
    sp=0;
    for i in range(0,len(M)):
        sp=sp+P[i]
        if random.random()<sp:
           return (M[i])
