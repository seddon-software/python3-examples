import subprocess, os, shutil

# copy files to staging area
shutil.rmtree("stage", ignore_errors = True)
shutil.copytree("src/mypackage", "stage/mypackage")
shutil.copy("src/setup.py", "stage")
                
os.chdir("stage")


# create a archive distribution 
subprocess.call("python setup.py sdist".split())

# create a windows self installer
subprocess.call("python setup.py bdist_wininst".split())

# create a linux self installer
subprocess.call("python setup.py bdist_rpm".split())
