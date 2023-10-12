from enums.ChartColor import ChartColor


class PlotData:
    """
    This class will contain all the data needed to plot using the Plotter class
    """

    def __init__(self):
        self.color = ChartColor.BLUE
        self.points = []
