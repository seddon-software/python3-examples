from single_step import s

s('cd myrepo')
s('git branch mybranch')
s('git checkout mybranch')
 
s('echo "branch file no. 1" > branch1.txt')
s('echo "branch file no. 2" > branch2.txt')
s('echo "branch file no. 3" > branch3.txt')
s('rm hello3.txt')
s('git add .') 
s('git commit -m "created a new branch"')
s('git push --set-upstream origin mybranch')

