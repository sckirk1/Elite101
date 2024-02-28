from main.utilities import FileSystemUtilities as fileUtils
import matplotlib.pyplot as plt


class Plotter:
    """
    This class wraps around matplotlib to plot the distributions for different dice rolls.
    Doing this to make sure I can switch libraries if needed and not refactor other classes relying on Plotter
    """

    X_AXIS_LABEL = 'Roll'
    Y_AXIS_LABEL = 'Probability'
    DEFAULT_PLOT_TITLE = 'Roll Distribution'

    def __init__(self, plotDatas=None, title=DEFAULT_PLOT_TITLE):
        if plotDatas is None:
            plotDatas = []
        self.__title = title
        self.__plotDatas = plotDatas

    def addAllData(self, datasToAdd):
        for data in datasToAdd:
            self.addData(data)

    def addData(self, dataToAdd):
        self.__plotDatas.append(dataToAdd)

    def removeData(self, dataToRemove):
        if dataToRemove in self.__plotDatas:
            self.__plotDatas.remove(dataToRemove)

    def __createFigure(self):
        figure, plot = plt.subplots()
        plot.set_title(self.__title)
        plot.set_xlabel(self.X_AXIS_LABEL)
        plot.set_ylabel(self.Y_AXIS_LABEL)
        for plotData in self.__plotDatas:
            plot.plot(plotData.getXValues(), plotData.getYValues(), color=plotData.getColor().value,
                      label=plotData.getName())
        plot.legend()
        return figure

    def showPlot(self):
        figure = self.__createFigure()
        figure.show()

    def savePlot(self, fileName):
        fileUtils.createOutDirectoryIfNotPresent()
        figure = self.__createFigure()
        figure.savefig(fileUtils.getFileOutputPath(self, fileName))