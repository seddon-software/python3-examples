############################################################
#
#    preserving tracebacks (doesn't work)
#
############################################################

import sys
import traceback

def doit():
    # some nested function encounters a problem
    raise RuntimeError('original error which must be reported ...')
    
def myfunct():
    try:
        doit()
    except:
        # if errorCorrection() fails it will mask out the original exception
        errorCorrection()

def errorCorrection():
    # the error correction code encounters a second exception
    # which potentially could mask the first exception
    raise RuntimeError('this error will mask original error ...')

try:
    myfunct()
except Exception, e:
    traceback.print_exc()

