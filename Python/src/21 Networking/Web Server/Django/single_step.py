import os, shutil
os.system("echo $PATH")
# site-packages/django/bin
import site
print(site.getsitepackages())
import sys
print(sys.path)
def s(*cmds):
    cmd = " ".join(cmds)
    print(">>>", cmd, end="")
    input()
    if cmd[0:2] == "cd":
        os.chdir(cmd[3:])
    else:
        os.system(cmd)

