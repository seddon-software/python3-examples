import os, sys

def setPaths():
    if sys.platform == "win32":
        swigPath = "C:/swigwin-2.0.9;"
        compilerPath = "C:/mingw/bin;"
        pythonPath = os.path.dirname(sys.executable) + ";"
    
    if sys.platform == "darwin":    # OSX 10.8
        swigPath = "/usr/local/bin:"
        compilerPath = "/opt/local/bin:"
        pythonPath = os.path.dirname(sys.executable) + ":"    
    
    if sys.platform == "linux2":
        swigPath = "/usr/local/bin:"
        compilerPath = "/usr/bin:"
        pythonPath = os.path.dirname(sys.executable) + ":"
    
    os.environ["PATH"] = pythonPath + swigPath + compilerPath + os.environ["PATH"]
setPaths()
