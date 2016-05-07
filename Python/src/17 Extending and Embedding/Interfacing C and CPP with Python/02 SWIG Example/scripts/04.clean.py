import os,shutil

os.chdir("../src")

try: os.remove('hello_wrap.c')
except: pass

try: os.remove('myhello.py')
except: pass

try: shutil.rmtree("build")
except: pass


print "staging area cleaned and temporary files removed"




