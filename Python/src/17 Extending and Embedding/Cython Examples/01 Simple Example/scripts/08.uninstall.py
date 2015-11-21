import os, sys, inspect
from distutils.sysconfig import get_python_lib, get_config_vars

def removeFiles(shared_object, directoryContainingModule, eggInfoFileName):
    try: os.remove(shared_object)
    except Exception, e: print e
    try: os.remove(directoryContainingModule + "/" + eggInfoFileName)
    except Exception, e: print e
        
name = 'MyCython_Package'
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
