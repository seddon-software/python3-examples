import os

os.chdir('myrepo')


password = raw_input("Enter password: ")
repo = "myrepo"
username = "seddon-software"
cmd = "git remote add origin https://{0}:{1}@github.com/{0}/{2}.git".format(username, password, repo)
os.system(cmd)
os.system('git remote -v')
os.system('git push -u origin master')

