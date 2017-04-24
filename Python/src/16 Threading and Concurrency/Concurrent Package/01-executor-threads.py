from concurrent.futures import ThreadPoolExecutor
import time

def work(x, y):
    print("this is the asynchronous call")
    time.sleep(10)
    return pow(x, y)
    
with ThreadPoolExecutor(max_workers=5) as executor:
    # make an asynchronous call
    future1 = executor.submit(work, 3, 5)
    future2 = executor.submit(work, 3, 6)
    print("this is the main thread waiting ...")
    print(future1.result())
    print(future2.result())
