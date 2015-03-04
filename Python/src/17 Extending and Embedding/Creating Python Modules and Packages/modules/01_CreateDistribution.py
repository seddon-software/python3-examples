import subprocess, os, shutil

# create staging area
if not os.path.exists("stage"): os.mkdir("stage")

# copy files to staging area
shutil.copy("src/mymodule.py", "stage")
shutil.copy("src/setup.py", "stage")


os.chdir("stage")

# create a archive distribution 
subprocess.call("python setup.py sdist".split())

# create a windows self installer
subprocess.call("python setup.py bdist_wininst".split())

# create a linux self installer
subprocess.call("python setup.py bdist_rpm".split())
