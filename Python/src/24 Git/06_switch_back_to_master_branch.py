import os

os.chdir('myrepo')

os.system('ls')
os.system('git checkout master')
os.system('ls')
os.system('echo "hello world" > hello4.txt')
os.system('echo "hello world" > hello5.txt')
os.system('echo "hello world" > hello6.txt')
os.system('git add .') 
os.system('git commit -m "more files for master branch"')
os.system('git push -u origin master')

