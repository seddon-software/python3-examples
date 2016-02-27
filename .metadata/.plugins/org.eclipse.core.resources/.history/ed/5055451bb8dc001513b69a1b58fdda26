############################################################
#
#    using runnable
#
############################################################

from threading import Thread
import random
import time
import sys

# create a runnable class
class MyClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        
    def run(self):
        for i in range (1, 50):
            sys.stdout.write(self.name)        
            time.sleep(random.random() * 0.1)    

m1 = MyClass("1")
m2 = MyClass("2")
m3 = MyClass("3")

# start calls run() polymorphically if no callback is specified
m1.start()
m2.start()
m3.start()

# wait for threads to complete
m1.join()
m2.join()
m3.join()

print "\nEnd of main"

1
