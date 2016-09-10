import timeit
from threading import Thread
from multiprocessing import Process

# work to be done
def SumRange(count):
    sum = 0
    for i in range (1, count):
        sum += i

# main job using threads
def job1(threads, iterations):
    threadList = []
    for i in range(threads):
        t = Thread(target = SumRange, args = (iterations,))
        t.start()
        threadList.append(t)        
    for t in threadList:
        t.join()

# main job using processes
def job2(processes, iterations):
    processesList = []
    for n in range(processes):
        p = Process(target=SumRange, args = (iterations,))
        p.start()
        processesList.append(p)
    for p in processesList:
        p.join()


# timings
setup1 = 'from __main__ import job1'
setup2 = 'from multiprocessing import Process; from __main__ import job2'

# try running same code in multiple threads compared with multiple processes
print("   {0:26s}  {1:26s}".format("using Threading", "using Processes"))
for i in (1, 2, 4, 8, 10, 20, 30, 50, 100, 250, 1000, 2000, 4000, 6000):
    n = (1000 * 1000)//i
    statement1 = 'job1(' + str(i) + ', ' + str(n) + ')'
    statement2 = 'job2(' + str(i) + ', ' + str(n) + ')'
    print("{0:6.3f} {1:20s}".format(timeit.Timer(statement1, setup1).timeit(1), statement1), end=' ')
    print("{0:6.3f} {1:20s}".format(timeit.Timer(statement2, setup2).timeit(1), statement2))
