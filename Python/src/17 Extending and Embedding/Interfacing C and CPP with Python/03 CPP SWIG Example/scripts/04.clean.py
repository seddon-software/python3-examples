import os,shutil
os.chdir("../src")

try: os.remove('myexample_wrap.cpp')
except: pass

try: os.remove('myexample.py')
except: pass

try: shutil.rmtree("build")
except: pass


print "staging area cleaned"


