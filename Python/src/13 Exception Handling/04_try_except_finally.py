############################################################
#
#    try-except-finally statements
#
############################################################

import sys

def f():
    raise RuntimeError('this is an error message')


try:
    f()
except Exception, e:
    print 'caught exception ...'
    print e.message
    print e
finally:
    print 'finally block ...'

1
