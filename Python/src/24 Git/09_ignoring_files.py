from single_step import s

s('cd myrepo')
s('echo f\* > .gitignore')
s('echo g\* >> .gitignore')
s('cat .gitignore')
s('git rm -r --cached .')
s('git add .')
s('git commit -am "Remove ignored files"')
s('git push -u origin master')
