import os, sys
from distutils.sysconfig import get_python_lib, get_config_vars

os.chdir(get_python_lib())
version = sys.version[0:3]
eggInfo = "SWIG_example-1.0-py" + version + ".egg-info"
sharedObject = "_myhello" + get_config_vars("SO")[0]
source = "myhello.py"
compiled = "myhello.pyc"

installedFiles = [eggInfo, sharedObject, source, compiled]

for item in installedFiles:
    try: os.remove(item)
    except Exception, e: print e

print
print "Example uninstalled"

