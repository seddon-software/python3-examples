############################################################
#
#    preserving tracebacks (does work)
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
        try:
            # re-raise the original error
            raise
        finally:
            # perform error correction in finally block
            # and handle any problems locally to avoid masking original exception
            try:
                errorCorrection()
            except:
                # report secondary exceptions
                traceback.print_exc()

def errorCorrection():
    # the error correction code encounters a second exception
    # which potentially could mask the first exception
    raise RuntimeError('this error must not mask original error ...')

try:
    myfunct()
except Exception, e:
    traceback.print_exc()

1
