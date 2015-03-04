############################################################
#
#    creating processes
#
############################################################

from subprocess import Popen

args = ("python", "childA.py", "Monday", "Tuesday", "Wednesday")
child = Popen(args)
child.wait()
print "child completed"



1