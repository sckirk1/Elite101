import os
import inspect

__PATH_TO_OUTPUT_DIRECTORY_FROM_UTILS = '../../../out'


def createOutDirectoryIfNotPresent():
    if not os.path.exists(__PATH_TO_OUTPUT_DIRECTORY_FROM_UTILS):
        os.mkdir(__PATH_TO_OUTPUT_DIRECTORY_FROM_UTILS)

def getPathToOutputDirectory(objectToOutput):
    filePath = inspect.getfile(objectToOutput)
    print(filePath)
