import os, shutil

# clean up previous runs
try:
    shutil.rmtree("myrepo")
except:
    pass    # no problem if repo doesn't exist

# create local repo
os.system('mkdir myrepo')
os.chdir('myrepo')
os.system('git init')

# add a README file and commit
os.system('echo "This is my new repo" > README.txt')
os.system('git add README.txt') 
os.system('git commit -m "first commit"')
