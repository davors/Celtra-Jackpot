class BanditGenerator() :
    intervals = [0]
    probabilities = [0.5]

    def pull(self,p) :
        for i in range(len(self.intervals)-1, -1, -1) :
            if p >= self.intervals[i] :
                if rand() <= self.probabilities[i] :
                    return 1
                else :
                    return 0

    def prob(self,p) :
        for i in range(len(self.intervals)-1, -1, -1) :
            if p >= self.intervals[i] :
                return self.probabilities[i]


class BanditTestCase() :
    
    onlineUrl = ''

    numBandits = 0
    maxPulls = 0
    maximumReward = 0

    bandits = []

    def __init__(self, url = '') :
        self.onlineUrl = url

    def pullBandit(self,bandit_id,pull_id) :
        if not self.onlineUrl :
            reward = self.bandits[bandit_id].pull[pull_id]
        else :
            reward = -1 #getMachineResponse(url,bandit_id,pull_id)
        return reward

    def getNumBandits(self) :
        if not self.onlineUrl :
            return self.numBandits
        else :
            #self.numBandits = getNumMachines(url)
            return -1 

    def getMaxPulls(self) :
        if not self.onlineUrl :
            return self.maxPulls
        else :
            #self.maxPulls = getNumPulls(url)
            return -1

    def calcMaxReward(self) :
        if self.onlineUrl :
            return -1

        self.maximumReward = 0.0
        for p in range(self.maxPulls) :
            max = 0.0
            for b in range(self.numBandits) :
                prob = self.bandits[b].prob(p)
                if(prob > max) :
                    max = prob
            self.maximumReward = self.maximumReward + max

        return self.maximumReward


