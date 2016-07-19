############################################################
#
#    creating processes
#
############################################################

from subprocess import Popen

args = ("python", "childB.py")
child = Popen(args)
child.wait()
print "child completed"

1
