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
except Exception as e:
    print('caught exception ...')
    print(e)
finally:
    print('finally block ...')

1
