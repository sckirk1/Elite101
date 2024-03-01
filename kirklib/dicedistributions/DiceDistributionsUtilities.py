from kirklib.plotter import Point
from kirklib.plotter import PlotData


def getPointsFromDistribution(distribution):
    points = []
    for rollProbability in distribution.getRollProbabilities():
        points.append(Point(rollProbability.getValue(), rollProbability.getProbability()))
    return points


def getPlotDataFromDistribution(distribution, color=None):
    plotData = PlotData(getPointsFromDistribution(distribution))
    return plotData
