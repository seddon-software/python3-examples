import subprocess,os,sys
import zipfile
import site
from distutils.sysconfig import get_python_lib

def setPath():
    # Changing the PATH to locate setuptools
    if sys.platform == 'darwin': offset = "/../../../bin:"
    if sys.platform == 'win32':  offset = "/../../Scripts;"
    if sys.platform == 'linux2': offset = "/../../../bin:"

    setuptoolsPath = get_python_lib() + offset
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]

def removeEggs():
    for dir in site.getsitepackages():
        version = str(sys.version[0:3])
        eggFile = dir + "/mymodule-1.0-py" + version + ".egg"
        try:
            os.remove(eggFile)
        except:
            pass
        else:
            print "removing " + eggFile
        
def cleanConfigFile():
    # remove entry from easy_install config file
    moduleName = "mymodule"
    cmd = "easy_install -m --allow-hosts=localhost:8000/repo " + moduleName
    subprocess.call(cmd.split())
    
setPath()
removeEggs()
cleanConfigFile()
