import random
class BanditGenerator() :
    intervals = None
    probabilities = None

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
    
    onlineUrl = None

    numBandits = None
    maxPulls = None
    maximumReward = None
    randomReward = None

    bandits = []

    def __init__(self, url = None) :
        self.onlineUrl = url

    def pullBandit(self,bandit_id,pull_id) :
        if (self.onlineUrl is None) :
            reward = self.bandits[bandit_id].pull(pull_id)
        else :
            reward = -1 #getMachineResponse(url,bandit_id,pull_id)
        return reward

    def getNumBandits(self) :
        if (self.onlineUrl is None) :
            return self.numBandits
        else :
            #self.numBandits = getNumMachines(url)
            return -1 

    def getMaxPulls(self) :
        if (self.onlineUrl is None) :
            return self.maxPulls
        else :
            #self.maxPulls = getNumPulls(url)
            return -1

    def calcMaxReward(self) :
        if not (self.onlineUrl is None) :
            return -1

        all_intervals = []
        for b in range(self.numBandits) :
            all_intervals += self.bandits[b].intervals
        all_intervals = sorted(set(all_intervals))
        all_intervals = all_intervals + [self.maxPulls]

        self.maximumReward = 0.0
        for i in range(len(all_intervals)-1) :
            best_reward = 0.0
            for b in range(self.numBandits) :
                prob = self.bandits[b].prob(all_intervals[i])
                if(prob > best_reward) :
                    best_reward = prob
            self.maximumReward += best_reward * (all_intervals[i+1] - all_intervals[i])

        return self.maximumReward

    def calcRandomReward(self) :
        if not (self.onlineUrl is None) :
            return -1

        self.randomReward = 0.0
        for b in range(self.numBandits) :
            self.randomReward += self.bandits[b].calcFullReward(self.maxPulls)
        self.randomReward /= self.numBandits

        return self.randomReward

