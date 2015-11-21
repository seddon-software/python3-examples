import sys, os, inspect
from distutils.sysconfig import get_python_lib


def displayInfo(directory, file):
    eggInfoFile = directory + "/" + file
    try:
        f = open(eggInfoFile, 'r')
        print f.read()
    except:
        print "can't get any info"

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
displayInfo(directoryContainingModule, eggInfoFileName)


