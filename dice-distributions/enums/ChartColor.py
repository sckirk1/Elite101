from enum import Enum

"""
This enum is used to relate color names to their respective named counterpart in matplotlib.
This is just for my own convenience and to try and limit the number of clashing contrasts.
"""
class ChartColor(Enum):
    BLUE = 'royalblue'
    RED = 'firebrick'
    GREEN = 'forestgreen'
    PURPLE = 'darkorchid'
    ORANGE = 'darkorange'
    PINK = 'palevioletred'
    BLACK = 'black'