import timeit
from threading import Thread
from multiprocessing import Process

# create a callable class
class MyClass:
    def __call__(self, count):
        sum = 0
        for i in range (1, count):
            sum += i        

# main job using threads
def job1(threadCount, iterations):
    threadList = []
    
    for i in range(1, threadCount+1):
        m = MyClass()
        t = Thread(target = m, args = (iterations,))
        t.start()
        threadList.append(t)
        
    for t in threadList:
        t.join()

# main job using processes
def job2P(iterations):
    m = MyClass()
    m(iterations)

# calls job1 with thread count = 1
def job2(processes, iterations):
    pid = []
    for n in range(processes):
        p = Process(target=job2P, args = (iterations,))
        pid.append(p)
        pid[n].start()
    
    for n in range(processes):
        pid[n].join()


setup1 = 'from __main__ import job1'
setup2 = 'from multiprocessing import Process; from __main__ import job2'

# try running same code in multiple threads compared with multiple processes
print "   {0:26s}  {1:26s}".format("using Threading", "using Processes")
for i in (1, 4, 8, 10, 20, 30, 50, 100, 250, 1000, 10000):
    n = 1000 * 1000/i
    statement1 = 'job1(' + str(i) + ', ' + str(n) + ')'
    statement2 = 'job2(' + str(i) + ', ' + str(n) + ')'
    print "{0:6.3f} {1:20s}".format(timeit.Timer(statement1, setup1).timeit(1), statement1),
    print "{0:6.3f} {1:20s}".format(timeit.Timer(statement2, setup2).timeit(1), statement2)



1
