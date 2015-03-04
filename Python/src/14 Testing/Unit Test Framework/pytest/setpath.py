import os,sys

def setPath():
    # Changing the PATH to locate py.test executable
    version = str(sys.version[0]) + str(sys.version[2])
    setuptoolsPath = "C:/Python" + version + "/Scripts;"
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]


setPath()
