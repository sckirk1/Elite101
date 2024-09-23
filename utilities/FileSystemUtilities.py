import os

__PATH_TO_OUTPUT_DIRECTORY = '../../out/reihtiwoehrtiowhe'


def createOutDirectoryIfNotPresent():
    if not os.path.exists(__PATH_TO_OUTPUT_DIRECTORY):
        os.mkdir(__PATH_TO_OUTPUT_DIRECTORY)
