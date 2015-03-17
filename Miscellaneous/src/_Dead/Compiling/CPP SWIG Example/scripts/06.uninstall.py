import os, sys

major = sys.version[0]
minor = sys.version[2]
version = sys.version[0:3]

sitePackages = "C:/Python" + str(major) + str(minor) + "/Lib/site-packages"
eggInfo = "CPP_SWIG_example-1.0-py" + version + ".egg-info"
os.chdir(sitePackages)
try: os.remove(eggInfo)
except: pass

try: os.remove('_myexample.pyd')
except: pass

try: os.remove('myexample.py')
except: pass

try: os.remove('myexample.pyc')
except: pass

print "Example uninstalled"


