
class machine(object):

    R=[]
    pulls=0
    pulls_total=0
    #self.last_pull=0
    #self.last_reset=0
    mean=0
    sum=0
    sum_total=0
    id=0
    moving_sum=[]
    variance=0
    def __var__(self,pulls):



        return var

        
    def __init__(self,id):
        self.R=[]
        self.pulls=0
        self.pulls_total=0
        #self.last_pull=0
        #self.last_reset=0
        self.mean=0
        self.sum=0
        self.sum_total=0
        self.id=id
        self.moving_sum=[]
        self.variance=0

    def update(self,r):
        self.R.append(r)
        self.pulls=self.pulls+1
        self.pulls_total=self.pulls_total+1
        self.sum=self.sum+r
        self.sum_total=self.sum_total+r
        self.mean=float(self.sum)/self.pulls
        

    def resetState(self,index,new_pulls):
        p_tmp=self.pulls-new_pulls
        self.sum=self.moving_sum[index]
        self.pulls=new_pulls
        self.mean=float(self.sum)/self.pulls
        self.moving_sum[index:]=[self.moving_sum[index]]*len(self.moving_sum[index:])
        return  p_tmp
        





