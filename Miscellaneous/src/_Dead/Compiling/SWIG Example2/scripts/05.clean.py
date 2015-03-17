import os,shutil

os.chdir("../src")

try: os.remove('hello_wrap.cpp')
except: pass

try: os.remove('hello.py')
except: pass

try: shutil.rmtree("build")
except: pass




