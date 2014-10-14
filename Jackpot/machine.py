from Config import *
import bisect
class machine(object):

    R=[]
    P=[]
    pulls=0
    pulls_total=0
    #self.last_pull=0
    #self.last_reset=0
    mean=0.0
    mean2=0.0
    sum=0
    sum_total=0
    id=0
    moving_sum=[]
    variance=0.0
    __M2__=0.0
    
    def __varmean__(self,pulls):
        n=self.pulls-pulls
        for x in self.R[-(pulls):]:
            n=n+1
            delta=x-self.mean
            self.mean=self.mean+float(delta)/n
            self.__M2__=self.__M2__+delta*(x-self.mean)

        if self.pulls<2:
            self.variance=0.0
        else:
            self.variance=float(self.__M2__)/(self.pulls-1)

        
    def __init__(self,id):
        self.R=[]
        self.P=[]
        self.pulls=0
        self.pulls_total=0
        #self.last_pull=0
        #self.last_reset=0
        self.mean=0.0
        self.mean2=0.0
        self.sum=0
        self.sum_total=0
        self.id=id
        self.moving_sum=[]
        self.variance=0.0
        __M2__=0.0

    def update(self,r,p):
        self.R.append(r)
        self.P.append(p)
        self.pulls=self.pulls+1
        self.pulls_total=self.pulls_total+1
        self.sum=self.sum+r
        self.sum_total=self.sum_total+r
        self.mean2=float(self.sum)/self.pulls
        self.__varmean__(1)
        

    def resetState(self,index,new_pulls):
        if index!=-2:
            if new_pulls>self.pulls:
                new_pulls=self.pulls
            p_tmp=self.pulls-new_pulls
            if index!=-1:
                self.moving_sum[index:]=[self.moving_sum[index]]*len(self.moving_sum[index:])
                self.sum=self.moving_sum[index]
            else:
                self.moving_sum[:]=[0.0]*len(self.moving_sum[index:])
                self.sum=0.0
        else:
            index=bisect.bisect(self.P,new_pulls)
            if index>0:
                new_pulls=len(R[index-1:])
                self.sum=sum(R[index-1:])
            else: 
                new_pulls=0
                self.sum=0

        self.pulls=new_pulls
        self.mean2=float(self.sum)/self.pulls
        self.mean=0.0;
        self.variance=0.0
        self.__M2__=0.0
        self.__varmean__(self.pulls)
        return  p_tmp
        





