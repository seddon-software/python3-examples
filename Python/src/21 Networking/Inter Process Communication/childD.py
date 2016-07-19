############################################################
#
#    childD
#
############################################################

# This client is executed as a child process of parent 
# with its stdin and stdout connected to thepipe.
# Thechild reads a message from the pipe (sent by the parent).
# The child then echoes the message back to the parent via the pipe.
  
import sys
input = sys.stdin.read()
sys.stdout.write('Client echoing message back to server: %s' % input)

