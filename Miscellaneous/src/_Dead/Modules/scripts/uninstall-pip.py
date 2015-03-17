import subprocess,os,sys, requests
import zipfile

def setPath():
    # Changing the PATH to locate setuptools
    setuptoolsPath = "C:/Python" + VV + "/Scripts;"
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]



VV = str(sys.version[0]) + str(sys.version[2])
setPath()
cmd = "pip uninstall mymodule"


# this has to be in a pipe
# because pip will ask a series of questions
proc = subprocess.Popen(cmd.split(),
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
# answer Yes to all pip questions
stdout_text = proc.communicate('y')[0]
print stdout_text
