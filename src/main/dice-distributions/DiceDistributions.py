from ..plotter.Plotter import Plotter
import DiceDistributionsUtilities as diceUtils


class DiceDistributions:

    def __init__(self):
        self.__plotter = Plotter()
        self.__distributions = []

    def addDistribution(self, distribution):
        self.__distributions.append(distribution)

    def plotDistributions(self):
        // fix
        self.__plotter.addAllData(diceUtils.getPlotDataFromDistribution(self.__distributions))
