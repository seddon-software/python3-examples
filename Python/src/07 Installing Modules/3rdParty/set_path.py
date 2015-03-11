import sys, os
from distutils.sysconfig import get_python_lib

def setPath():
    # Changing the PATH to locate setuptools
    if sys.platform == 'darwin': setuptoolsPath = get_python_lib() + "/../../../Frameworks/Python.framework/Versions/2.7/bin:"
    if sys.platform == 'win32':  setuptoolsPath = get_python_lib() + "/../../Scripts;"
    if sys.platform == 'linux2': setuptoolsPath = get_python_lib() + "/../../../bin:"

    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]

setPath()

