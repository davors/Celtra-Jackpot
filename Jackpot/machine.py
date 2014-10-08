
class machine(object):
    id=0
    N=0
    R=[]
    Nlast=0
    mR=0
    sR=0
    totalReward=0
    totalN=0
        
    def __init__(self,id,max_pulls):
        self.R=[]
        self.N=0
        self.Nlast=0
        self.mR=0
        self.sR=0
        self.totalReward=0
        self.id=id

    def pull(self,r):
        self.R.append(r)
        self.N=self.N+1
        self.Nlast=self.Nlast+1
        self.sR=self.sR+r
        self.totalReward=self.totalReward+r
        self.mR=float(self.sR)/self.N
        self.totalN=self.totalN+1

    def resetState(self):
        self.Nlast=self.N
        self.N=0
        self.R=[]
        self.Nlast=0
        self.mR=0
        self.sR=0
        return 0





