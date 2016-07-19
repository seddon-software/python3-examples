import os, shutil

os.chdir("C:/Python26/Lib/site-packages")
os.remove("mypackage-1.0-py2.6.egg-info")
shutil.rmtree("mypackage")
