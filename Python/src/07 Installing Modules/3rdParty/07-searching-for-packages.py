import subprocess,os,sys
from distutils.sysconfig import get_python_lib

def setPath():
    # Changing the PATH to locate setuptools
    if sys.platform == 'darwin': offset = "/../../../bin:"
    if sys.platform == 'win32':  offset = "/../../Scripts;"
    if sys.platform == 'linux2': offset = "/../../../bin:"

    setuptoolsPath = get_python_lib() + offset
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]

def setProxy(url):
    """example call:
          setProxy("http://wwwcache.rl.ac.uk:8080")
    """
    os.environ["HTTP_PROXY"] = url
    
def install(cmd):
    cmd = (installer + " " + cmd)
    print "****", cmd
    subprocess.call(cmd.split())
    
setPath()
subprocess.call(r"pip search ' git '".split())

1



