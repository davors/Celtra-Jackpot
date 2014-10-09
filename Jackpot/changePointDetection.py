#
# Statistical tests to determine if the machine changed
#

from math import *

#rat=kumulativen povprecen reward na avtomat v t potezah
#rt=sestevek rewardow do t
#delta toleranca

#PH0=M0-m0=0
#PHt=Mt-mt=max(PH(t-1)-rt+rat-delta,0)

#Treshold 80
def HankeyPankeyTest(Tsh,mt, Mt,X, Y, N):
    delta=0.005
    if N==0:
        HP=0.0
        Y=0.0
        Mt=0
        mt=0
    Y=Y+X
    mt=0.9999*mt+float(X)-float(Y)/float(N)+delta
    #mt=0.9999*mt+float(Y)/float(N)-X+delta
    Mt=max(Mt,mt)
    #HP=max(float(HP)-float(X)+float(Y)/float(N)-delta,0)
    HP=Mt-mt
    print str(HP)
    return (HP>Tsh, mt, Mt, Y)



def checkChange(Tsh, m):
    # tp=range(3,10) + range(10,100,10) + range(100,1000,100)
    tp=[50] 
    if m.moving_sum==[]:
        m.moving_sum=[0.0 for s in tp]
    for t in range(0,len(tp)):
        s=tp[t]
        if s<m.pulls:
            m.moving_sum[t]=m.moving_sum[t]-m.R[-(s+1)]
        m.moving_sum[t]=m.moving_sum[t]+m.R[-1]
        if s>m.pulls:
            s=m.pulls
        Z=testIfDistDiff(m.sum,m.moving_sum[t],m.pulls,s)
        #print str(Z)
        # 95 % confidence interval
        if Z>=Tsh:
            print 'checkChange triggered at: '+str((Z,m.id,m.pulls))
            m.resetState(t,s)
    return m
            




def testIfDistDiff(X,Y,Nx,Ny):
    try:
        Z=abs(((float(X)/Nx)-(float(Y)/Ny))/sqrt((float(X)+float(Y))/(float(Nx)+float(Ny))*(1.0-(float(X)+float(Y))/(float(Nx)+float(Ny)))*(1.0/float(Nx)+1.0/Ny)))
    except:
        Z=0.0
    return Z

def testIfSampleDiff(X,Y,Nx,Ny):

    Z1=sqrt((Nx*(X/Nx-Y/Ny)**2)/(X/Nx*(1-X/Nx)+0.00001))/2
    Z2=sqrt((Ny*(X/Nx-Y/Ny)**2)/(Y/Ny*(1-Y/Ny)+0.00001))/2

    Z=min(Z1,Z2)
    return Z

 