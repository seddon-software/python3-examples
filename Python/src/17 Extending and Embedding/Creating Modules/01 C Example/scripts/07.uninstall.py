import os, sys
from distutils.sysconfig import get_python_lib, get_config_vars

os.chdir(get_python_lib())
version = sys.version[0:3]
eggInfo = "FibonacciPackage-1.0-py" + version + ".egg-info"
shared_object = "fibonacci" + get_config_vars("SO")[0]

try: os.remove(eggInfo)
except Exception, e: print e

try: os.remove(shared_object)
except Exception, e: print e


print "Example uninstalled"


