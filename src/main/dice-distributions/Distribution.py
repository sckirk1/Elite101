
class Distribution:

    def __init__(self, rollProbabilities=None):
        if rollProbabilities is None:
            rollProbabilities = []
        self.__rollProbabilities = rollProbabilities
        self.distributionName = ''

    def getRollProbabilities(self):
        return self.__rollProbabilities
