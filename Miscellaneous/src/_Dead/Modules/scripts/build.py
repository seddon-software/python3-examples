import subprocess, os, sys, shutil


os.chdir("../src")

# create source distro
subprocess.call("python setup.py sdist".split())

# move to local repo
shutil.move("dist/mymodule-1.0.zip", "../server/repo")
