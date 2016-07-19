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

# import sqlite3


os.chdir(baseDir)
# conn = sqlite3.connect("db.sqlite3")
os.chdir(projectDir)
# os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
subprocess.call("python manage.py startapp polls".split())




