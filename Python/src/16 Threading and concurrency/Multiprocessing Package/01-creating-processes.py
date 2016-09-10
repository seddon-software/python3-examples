from multiprocessing import Process

def square(x):
    print(x**2)

p = Process(target=square, args=(25,))
p.start()
p.join()
    