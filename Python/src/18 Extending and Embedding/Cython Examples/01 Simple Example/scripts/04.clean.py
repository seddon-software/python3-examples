import os, shutil
import subprocess

os.chdir("../src")

subprocess.call("rm hello.c hello.so".split())

try: shutil.rmtree("build")
except: pass

print "staging area cleaned"


