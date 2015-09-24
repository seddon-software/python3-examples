import os, sys, inspect
from distutils.sysconfig import get_python_lib, get_config_vars

# os.chdir(get_python_lib())
# version = sys.version[0:3]
# eggInfo = "FibonacciPackage-1.0-py" + version + ".egg-info"
# shared_object = "fibonacci" + get_config_vars("SO")[0]
# 
# try: os.remove(eggInfo)
# except Exception, e: print e
# 
# try: os.remove(shared_object)
# except Exception, e: print e
# 
# 
# print "Example uninstalled"

def removeFiles(shared_object, directoryContainingModule, eggInfoFileName):
    try: os.remove(shared_object)
    except Exception, e: print e
    try: os.remove(directoryContainingModule + "/" + eggInfoFileName)
    except Exception, e: print e
        

name = 'HelloWorld_Package'
moduleVersion = '2.0'

try:
    import hello
except:
    print "module not installed"
    sys.exit()

# determine the location of the imported module
shared_object = inspect.getabsfile(hello)
directoryContainingModule = os.path.dirname(shared_object)
pythonVersion = str(sys.version[0:3])
eggInfoFileName = "{}-{}-py{}.egg-info".format(name, moduleVersion, pythonVersion)

removeFiles(shared_object, directoryContainingModule, eggInfoFileName)
