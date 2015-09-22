import subprocess, os, sys, shutil


os.chdir("../src")

# create source distro
subprocess.call("python setup.py sdist --formats=zip".split())

# copy to local repo
shutil.copy("dist/mymodule-1.0.zip", "../server/repo")
print "\n", "mymodule-1.0.zip", "copied to local repo"