import timeit, time
from multiprocessing import Pool
import urllib.request


def timing(setup, fn, count):
    print("{:8d} {:6.3f} {:20s}".format(count, timeit.Timer(fn, setup).timeit(number=count), fn))
    time.sleep(5)
    
def download(url):
    response = urllib.request.urlopen('http://python.org/')
    html = response.read()
    html = html.decode('UTF-8')
#     print(html)
    return html
    
def parallel(poolSize):    
    urls = [
        'http://www.python.org', 
        'http://www.python.org/about/',
        'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
        'http://www.python.org/doc/',
        'http://www.python.org/download/',
        'http://www.python.org/getit/',
        'http://www.python.org/community/',
        'https://wiki.python.org/moin/',
        'http://planet.python.org/',
        'https://wiki.python.org/moin/LocalUserGroups',
        'http://www.python.org/psf/',
        'http://docs.python.org/devguide/',
        'http://www.python.org/community/awards/'
      ]
    pool = Pool(poolSize)
    try:
        # n.b. pool.map tries to pickle results
        # and the return from urllib.request.urlopen can't be pickled
        # so can't call urllib.request.urlopen directly
        pool.map(download, urls) 
    except Exception as e:
        print(e)

PARALLEL_1 = 'parallel(1)'
PARALLEL_2 = 'parallel(2)'
PARALLEL_3 = 'parallel(3)'
PARALLEL_4 = 'parallel(4)'
PARALLEL_8 = 'parallel(8)'
PARALLEL_16 = 'parallel(16)'

print("{:>8s} {:>6s} {:20s}".format("count", "time", "call"))
print("{:>8s} {:>6s} {:20s}".format("=====", "====", "===="))

count = 1
setupPARALLEL = 'from __main__ import parallel'
timing(setupPARALLEL, PARALLEL_1, count)
timing(setupPARALLEL, PARALLEL_2, count)
timing(setupPARALLEL, PARALLEL_3, count)
timing(setupPARALLEL, PARALLEL_4, count)
timing(setupPARALLEL, PARALLEL_8, count)
timing(setupPARALLEL, PARALLEL_16, count)

count = 5
timing(setupPARALLEL, PARALLEL_1, count)
timing(setupPARALLEL, PARALLEL_2, count)
timing(setupPARALLEL, PARALLEL_3, count)
timing(setupPARALLEL, PARALLEL_4, count)
timing(setupPARALLEL, PARALLEL_8, count)
timing(setupPARALLEL, PARALLEL_16, count)
