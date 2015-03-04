import subprocess,os,sys

def setPath():
    # Changing the PATH to locate nose executable
    version = str(sys.version[0]) + str(sys.version[2])
    setuptoolsPath = "C:/Python" + version + "/Scripts;"
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]
    print os.environ["PATH"]


setPath()
subprocess.call("nosetests -v".split())

    


