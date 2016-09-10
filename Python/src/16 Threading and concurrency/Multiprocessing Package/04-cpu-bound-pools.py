import timeit
from multiprocessing import Pool
import time


def timing(setup, fn, count):
    print("{:8d} {:6.3f} {:20s}".format(count, timeit.Timer(fn, setup).timeit(number=count), fn))
    time.sleep(5)

def cpuBoundFunction(x):
    i = 0
    for x in range(1000000): i = i + 1
    return x + 1

def serial():
    serialList = []
    r = range(100)
    for i in r: serialList += [cpuBoundFunction(i)]

def parallel(poolSize):
    parallelList = []
    pool = Pool(poolSize)
    r = range(100)
    parallelList = pool.map(cpuBoundFunction, r) 

SERIAL = 'serial()'
PARALLEL_1 = 'parallel(1)'
PARALLEL_2 = 'parallel(2)'
PARALLEL_3 = 'parallel(3)'
PARALLEL_4 = 'parallel(4)'
PARALLEL_8 = 'parallel(8)'
PARALLEL_16 = 'parallel(16)'

print("{:>8s} {:>6s} {:20s}".format("count", "time", "call"))
print("{:>8s} {:>6s} {:20s}".format("=====", "====", "===="))

count = 1
setupSERIAL = 'from __main__ import serial, cpuBoundFunction'
setupPARALLEL = 'from __main__ import parallel, cpuBoundFunction'
timing(setupSERIAL, SERIAL, count)
timing(setupPARALLEL, PARALLEL_1, count)
timing(setupPARALLEL, PARALLEL_2, count)
timing(setupPARALLEL, PARALLEL_3, count)
timing(setupPARALLEL, PARALLEL_4, count)
timing(setupPARALLEL, PARALLEL_8, count)
timing(setupPARALLEL, PARALLEL_16, count)

count = 5
timing(setupSERIAL, SERIAL, count)
timing(setupPARALLEL, PARALLEL_1, count)
timing(setupPARALLEL, PARALLEL_2, count)
timing(setupPARALLEL, PARALLEL_3, count)
timing(setupPARALLEL, PARALLEL_4, count)
timing(setupPARALLEL, PARALLEL_8, count)
timing(setupPARALLEL, PARALLEL_16, count)
