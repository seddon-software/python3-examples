import sys
from single_step import s

# create local repo
def windows():
    s('deltree myrepo')
    s('md myrepo')
    s('cd myrepo')
    s('git init')
    
    # add a README file and commit
    s('echo "This is my new repo" > README.txt')
    s('git add README.txt') 
    s('git commit -m "first commit"')

def unix():
    s('rm -rf myrepo')
    s('mkdir myrepo')
    s('cd myrepo')
    s('git init')
    
    # add a README file and commit
    s('echo "This is my new repo" > README.txt')
    s('git add README.txt') 
    s('git commit -m "first commit"')


if sys.platform == "win32":
    windows()
else:
    unix()
