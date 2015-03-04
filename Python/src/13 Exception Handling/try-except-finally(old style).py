############################################################
#
#    try-except-finally statements
#
############################################################

import sys

def f():
    raise RuntimeError('this is an error message')


try:
    try:
        f()
    except Exception, e:
        print 'caught exception ...'
finally:
    print 'finally block ...'

