import sys
from cStringIO import StringIO

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

# blah blah lots of code ...
print "abc"

sys.stdout = old_stdout

print mystdout.getvalue()
