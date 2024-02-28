import os
import inspect

__OUTPUT_DIRECTORY_NAME = 'out'
__PATH_TO_OUTPUT_DIRECTORY_FROM_UTILS = '..' + os.sep + '..' + os.sep + __OUTPUT_DIRECTORY_NAME


def createOutDirectoryIfNotPresent():
    if not os.path.exists(__PATH_TO_OUTPUT_DIRECTORY_FROM_UTILS):
        os.mkdir(__PATH_TO_OUTPUT_DIRECTORY_FROM_UTILS)


def getFileOutputPath(objectWritingToFileSystem, fileName):
    filePath = inspect.getfile(objectWritingToFileSystem.__class__)
    pathList = filePath.split(os.sep)[::-1]
    pathList.pop(0)  # Ignore the file, only look at directories
    outputPath = ''
    for directory in pathList:
        outputPath += '..' + os.sep
        if directory == 'main':
            return outputPath + __OUTPUT_DIRECTORY_NAME + os.sep + fileName
