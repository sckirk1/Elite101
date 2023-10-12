from enums.ChartColor import ChartColor

"""
This class will contain all the data needed to plot using the Plotter class
"""


class PlotData:

    def __init__(self):
        self.color = ChartColor.BLUE
        self.points = []
