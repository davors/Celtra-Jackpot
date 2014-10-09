#Different strategies for tackling the problem
import random
import machine
import math
from sys import maxfloat

#the UCB algorithm by Auer et al., 2002
def UCB1(actions, all_pulls, parC = 1.0):
    
    selectedAction = None
    bestVal = -maxfloat

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
                if selectedAction is not None :
                    if random.random() < 0.5 :
                        selectedAction = a
                else :
                    selectedAction = a

    return selectedAction


def UCBT():
    return 0



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
