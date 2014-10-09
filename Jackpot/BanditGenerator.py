import random
class BanditGenerator() :
    intervals = [0]
    probabilities = [0.5]

    def pull(self,p) :
        for i in range(len(self.intervals)-1, -1, -1) :
            if p >= self.intervals[i] :
                if random.random() < self.probabilities[i] :
                    return 1.0
                else :
                    return 0.0

    def prob(self,p) :
        for i in range(len(self.intervals)-1, -1, -1) :
            if p >= self.intervals[i] :
                return self.probabilities[i]

    def calcFullReward(self, max_pulls) :
        fullReward = 0.0
        endInterval = max_pulls
        for i in range(len(self.intervals)-1, -1, -1) :
            if(endInterval >= self.intervals[i]) :
                fullReward += self.probabilities[i] * (endInterval - self.intervals[i])
            endInterval = self.intervals[i]
        return fullReward

class BanditTestCase() :
    
    onlineUrl = ''

    numBandits = 0
    maxPulls = 0
    maximumReward = 0.0
    randomReward = 0.0

    bandits = []

    def __init__(self, url = '') :
        self.onlineUrl = url

    def pullBandit(self,bandit_id,pull_id) :
        if not self.onlineUrl :
            reward = self.bandits[bandit_id].pull(pull_id)
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

    def calcRandomReward(self) :
        if self.onlineUrl :
            return -1

        self.randomReward = 0.0
        for b in range(self.numBandits) :
            self.randomReward += self.bandits[b].calcFullReward(self.maxPulls)
        self.randomReward /= self.numBandits

        return self.randomReward

