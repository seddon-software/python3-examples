from concurrent.futures import ProcessPoolExecutor
import time

def work(x, y):
    print("this is the asynchronous call")
    time.sleep(5)
    return pow(x, y)
    
with ProcessPoolExecutor(max_workers=1) as executor:
    # make an asynchronous call
    #future = executor.submit(pow, 323, 1235)
    future = executor.submit(work, 323, 1235)
    print("this is the main thread waiting ...")
    print(future.result())
