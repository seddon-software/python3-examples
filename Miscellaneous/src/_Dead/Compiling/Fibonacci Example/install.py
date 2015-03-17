# run build first

import subprocess,os,sys

def setPath():
    # Changing the PATH to locate C compiler
    mingwPath = "C:\mingw\bin;"
    os.environ["PATH"] = mingwPath + os.environ["PATH"]

setPath()
os.chdir("src")

subprocess.call("python setup.py install".split())
