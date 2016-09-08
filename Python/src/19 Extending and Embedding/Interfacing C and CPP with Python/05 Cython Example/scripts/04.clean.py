import os, shutil

os.chdir("../src")
os.system("rm functions.c *.so")

try: shutil.rmtree("build")
except: pass

print("staging area cleaned")


