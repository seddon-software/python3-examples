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
    os.environ["PATH"] = sys.executable + os.pathsep + os.environ["PATH"]

print sys.executable
setPath()
baseDir = "webapp"
projectDir = "mysite"

os.chdir(baseDir)
os.chdir(projectDir)


# settings file is 'Django/mysettings.py' and 'Django/__init__.py must exist
os.environ["DJANGO_SETTINGS_MODULE"] = "Django.mysettings"

subprocess.call("python manage.py runserver".split())

# create the neccessary directory
if not os.path.exists(baseDir): os.makedirs(baseDir)
os.chdir(baseDir)

# run the setup command
if not os.path.exists(projectDir):
    subprocess.call(["django-admin.py", "startproject", projectDir])
    print "project {0} is now set up".format(projectDir)
else:
    print "project {0} already exists".format(projectDir)




