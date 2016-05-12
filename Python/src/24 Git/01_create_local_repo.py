from single_step import s

# create local repo
s('rm -rf myrepo')
s('mkdir myrepo')
s('cd myrepo')
s('git init')

# add a README file and commit
s('echo "This is my new repo" > README.txt')
s('git add README.txt') 
s('git commit -m "first commit"')
