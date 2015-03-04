import subprocess, os, sys
from distutils.sysconfig import get_python_lib

def setPath():
    # Changing the PATH to locate setuptools
    if sys.platform == 'darwin': offset = "/../../../bin:"
    if sys.platform == 'win32':  offset = "/../../Scripts;"
    if sys.platform == 'linux2': offset = "/../../../bin:"

    setuptoolsPath = get_python_lib() + offset
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]
    
setPath()
moduleName = "mymodule-1.0.zip"
cmd = "pip install http://localhost:8000/repo/" + moduleName
print cmd
subprocess.call(cmd.split())

