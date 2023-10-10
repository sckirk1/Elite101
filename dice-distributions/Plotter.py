import matplotlib.pyplot as plt

"""
This class wraps around matplotlib to plot the distributions for different dice rolls.
Doing this to make sure I can switch libraries if needed and not refactor other classes relying on Plotter
"""
class Plotter:
    def __init__(self):
        self.title = 'Title'