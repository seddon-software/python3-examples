import timeit, time
from concurrent.futures import ThreadPoolExecutor

# note this routine uses the GIL sparingly
x = [25]
def sleep(): 
    x.append(100)
    time.sleep(5)
    print(x)

# work with threads
def job(number):
    with ThreadPoolExecutor(max_workers=number) as e:
        for n in range(number):
            e.submit(sleep)

# will this take 5 secs or 40 times as long?
timer = timeit.Timer('job(40)', 'from __main__ import job')
t = timer.timeit(number=1)
print("Time for 40 calls: {:.2f}".format(t))

