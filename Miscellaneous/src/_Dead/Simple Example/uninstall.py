import os, sys

major = sys.version[0]
minor = sys.version[2]
version = sys.version[0:3]

sitePackages = "C:/Python" + str(major) + str(minor) + "/Lib/site-packages"
eggInfo = "SimpleExample-1.0-py" + version + ".egg-info"

try:
    os.chdir(sitePackages)
    os.remove(eggInfo)
    os.remove('hello.pyd')
    print "Example uninstalled"
except:
    print "Example appears to be already uninstalled"

