from multiprocessing import Process, Queue

def square(q, x):
    q.put(x**2)

def f(q):
    q.put([42, None, 'hello'])

q = Queue()
p = Process(target=square, args=(q, 25))
p.start()
print(q.get())
p.join()
