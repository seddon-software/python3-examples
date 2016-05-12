import os, shutil

def s(*cmds):
    cmd = " ".join(cmds)
    print ">>>", cmd,
    raw_input()
    if cmd[0:2] == "cd":
        os.chdir('myrepo')
    else:
        os.system(cmd)

