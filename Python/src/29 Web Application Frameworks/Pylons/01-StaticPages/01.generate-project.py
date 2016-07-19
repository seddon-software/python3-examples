import subprocess,os,sys

def setPath():
    # Changing the PATH to locate scripts
    version = str(sys.version[0]) + str(sys.version[2])
    scriptsPath = "C:/Python" + version + "/Scripts;"
    os.environ["PATH"] = scriptsPath + os.environ["PATH"]


setPath()
subprocess.call("paster create --template=pylons --view-template=mako StaticPages")
#subprocess.call("paster create --help")
