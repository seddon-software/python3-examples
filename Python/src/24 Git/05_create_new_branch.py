import os

os.chdir('myrepo')

os.system('git branch mybranch')
os.system('git checkout mybranch')
 
os.system('echo "branch file no. 1" > branch1.txt')
os.system('echo "branch file no. 2" > branch2.txt')
os.system('echo "branch file no. 3" > branch3.txt')
os.system('rm hello3.txt')
os.system('git add .') 
os.system('git commit -m "created a new branch"')
os.system('git push --set-upstream origin mybranch')

