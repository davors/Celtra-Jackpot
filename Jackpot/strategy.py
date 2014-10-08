#Different strategies for tackling the problem
import random

def UCB1():
    return 0


def UCBT():
    return 0



def EGreedy(M, E):
    Avg=[m.mR for m in M]
    maxM=Avg.index(max(Avg))
    P=[float(E)/len(M)]*len(M)
    P[maxM]=1-E+E/len(M)
    sp=0;
    for i in range(0,len(M)):
        sp=sp+P[i]
        if random.random()<sp:
           return (M[i])
