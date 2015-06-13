#!/usr/bin/env python

import threading
import datetime
import time

def  myTime():
    now = datetime.datetime.today().isoformat()
    print "Timer time {}".format(now)
    
now = datetime.datetime.today().isoformat()
print "Start time {}".format(now)

t = threading.Timer(3, myTime)
t.start()

now = datetime.datetime.today().isoformat()
print "End time {}".format(now)

