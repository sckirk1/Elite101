from enums import ChartColor


class PlotData:
    """
    This class will contain all the data needed to plot using the Plotter class
    """

    DEFAULT_DATA_NAME = 'Dice Roll'
    DEFAULT_DATA_COLOR = ChartColor.BLUE

    def __init__(self, points=None, color=DEFAULT_DATA_COLOR, name=DEFAULT_DATA_NAME):
        if points is None:
            points = []
        self.__points = points
        self.__color = color
        self.__name = name

    def getXValues(self):
        xPoints = []
        for point in self.__points:
            xPoints.append(point.getX())
        return xPoints

    def getYValues(self):
        yPoints = []
        for point in self.__points:
            yPoints.append(point.getY())
        return yPoints

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color
