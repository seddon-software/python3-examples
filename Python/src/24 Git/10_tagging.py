import sys
from single_step import s


def tagIt(tagId):
    s('git add .')
    s('git commit -m "added files about to be tagged"')
    s('git log --pretty=oneline')
    commitId = raw_input('\nenter the first 10 characters of the commit id to tag: ')
    s('git tag', tagId, commitId)
    s('git show-ref --tags')
    
def windows():
    s('cd myrepo')
    s('copy nul > f1')
    s('copy nul > f2')
    s('copy nul > f3')
    s('copy nul > f4')
    tagIt('1.0.0')
    s('copy nul > g1')
    s('copy nul > g2')
    s('copy nul > g3')
    s('copy nul > g4')
    tagIt('1.0.1')
    s('copy nul > h1')
    s('copy nul > h2')
    s('copy nul > h3')
    s('copy nul > h4')
    tagIt('1.0.2')

def unix():
    s('cd myrepo')
    s('touch f1 f2 f3 f4')
    tagIt('1.0.0')
    s('touch g1 g2 g3 g4')
    tagIt('1.0.1')
    s('touch h1 h2 h3 h4')
    tagIt('1.0.2')


if sys.platform == "win32":
    windows()
else:
    unix()
