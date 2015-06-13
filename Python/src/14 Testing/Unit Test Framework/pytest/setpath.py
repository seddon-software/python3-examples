import os,sys

def setPath():
    # Changing the PATH to locate py.test executable
    version = str(sys.version[0]) + str(sys.version[2])
    pytestPath = "/Library/Frameworks/Python.framework/Versions/2.7/bin:"
    os.environ["PATH"] = pytestPath + os.environ["PATH"]


setPath()
