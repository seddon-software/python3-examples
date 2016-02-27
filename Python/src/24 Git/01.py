import os

os.system('mkdir myrepo')
os.chdir('myrepo')

os.system('git init')
os.system('echo "hello world" > hello.txt')
os.system('git add hello.txt') 
os.system('git status')
os.system('git commit -m "added hello.txt"')
os.system('git status')
os.system('git log')
os.system('git show')
os.system('git remote add origin https://github.com/seddon-software/sat-repo.git')
os.system('git remote -v')
os.system('git push -u origin master')

