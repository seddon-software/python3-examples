import subprocess, os, sys

def setPath():
    # Changing the PATH to locate setuptools
    version = str(sys.version[0]) + str(sys.version[2])
    setuptoolsPath = "C:/Python" + version + "/Scripts;"
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]


setPath()
moduleName = "mymodule"
cmd = "easy_install -f http://localhost:8000/repo --allow-hosts=localhost:8000 " + moduleName
print cmd
subprocess.call(cmd.split())

