############################################################
#
#    Pipes
#
############################################################

# Parent creates a child with the child's stdin and stdout connected to the pipe
#  The parent sends a message to the pipe and reads a reply from the pipe.

args = ("python", "childD.py")
import subprocess

proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
messageFromClient = proc.communicate("This is a message from the parent")[0]
print messageFromClient

