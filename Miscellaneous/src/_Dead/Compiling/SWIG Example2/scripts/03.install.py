import subprocess,os,sys

def setPath():
    # Changing the PATH to locate SWIG
    swigPath = "C:\swigwin-2.0.2;"
    mingwPath = "C:\mingw\bin;"
    os.environ["PATH"] = swigPath + mingwPath + os.environ["PATH"]

setPath()
os.chdir("../src")

# must run build.py first
subprocess.call("python setup.py install".split())
