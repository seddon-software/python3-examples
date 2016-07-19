import subprocess,os,sys
from distutils.sysconfig import get_python_lib
import django
import django.core.handlers.wsgi


def setPath():
    # Changing the PATH to locate django binaries
    if sys.platform == 'darwin': offset = "/django/bin:"
    if sys.platform == 'win32':  offset = "/?????;"
    if sys.platform == 'linux2': offset = "/django/bin:"
    djangoBinaries = get_python_lib() + offset
    os.environ["PATH"] = djangoBinaries + os.environ["PATH"]

setPath()
print django.get_version()

baseDir = "webapp2"
projectDir = "mysite"
# settings file is 'Django/mysettings.py' and 'Django/__init__.py must exist
os.environ["DJANGO_SETTINGS_MODULE"] = "Django.mysettings"


# create the neccessary directory
if not os.path.exists(baseDir): os.makedirs(baseDir)
os.chdir(baseDir)

# run the setup command

# p = subprocess.Popen(['grep','f'],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
# >>> p.stdin.write('one\ntwo\nthree\nfour\nfive\nsix\n')
# >>> p.communicate()[0]
# 'four\nfive\n'
# >>> p.stdin.close()

if not os.path.exists(projectDir):
    def doIt():
        p = subprocess.Popen(["django-admin.py", "startproject", projectDir],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        p.communicate()[0]
    
    doIt()  
    # subprocess.call(["django-admin.py", "startproject", projectDir])
    print "project {0} is now set up".format(projectDir)
else:
    print "project {0} already exists".format(projectDir)



