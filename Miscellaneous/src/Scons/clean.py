import subprocess, os, sys

def setPath():
    # Changing the PATH to locate setuptools
    sconsPath = "C:/Python26/Scripts;"
    os.environ["PATH"] = sconsPath + os.environ["PATH"]

setPath()    
os.chdir("res")
subprocess.call("scons.bat -c -f makefile.py".split())
