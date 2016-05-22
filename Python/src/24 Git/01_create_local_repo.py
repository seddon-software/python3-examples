import sys
from single_step import s

# create local repo
if sys.platform == "win32":
    s('deltree myrepo')
    s('md myrepo')
else:
    s('rm -rf myrepo')
    s('mkdir myrepo')
s('cd myrepo')
s('git init')

# add a README file and commit
s('echo "This is my new repo" > README.txt')
s('git add README.txt') 
s('git commit -m "first commit"')
