import os,shutil

os.chdir("../src")

try: shutil.rmtree("build")
except: pass

print "staging area cleaned"


