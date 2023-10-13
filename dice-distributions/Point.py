class Point:
    """
    This class is just a POJO, plain old Java object (or I guess POPO in this case)
    It contains an X and a Y value, so we do not need to keep track of a pair of lists when trying to plot.
    Instead, we can just keep a single list of Points
    """

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
