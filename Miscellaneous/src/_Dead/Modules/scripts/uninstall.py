import subprocess,os,sys, requests
import zipfile

def setPath():
    # Changing the PATH to locate setuptools
    setuptoolsPath = "C:/Python" + VV + "/Scripts;"
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]

VV = str(sys.version[0]) + str(sys.version[2])
VVV = str(sys.version[0:3])
setPath()
moduleName = "mymodule"
cmd = "easy_install -m --allow-hosts=localhost:8000/repo " + moduleName
subprocess.call(cmd.split())
eggFile = "mymodule-1.0-py" + VVV + ".egg"
eggFile = "C:/Python" + VV + "/Lib/site-packages/" + eggFile
print "removing:", eggFile
try:
    os.remove(eggFile)
except:
    pass

