import sys
import os


def addRootPath():
    folder = os.path.split(os.path.realpath(__file__))[0]
    workspace = folder
    sys.path.append(workspace)
    return workspace


workspace = addRootPath()
