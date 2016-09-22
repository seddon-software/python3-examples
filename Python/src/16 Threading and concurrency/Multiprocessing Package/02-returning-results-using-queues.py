from multiprocessing import Process, Queue
def square(q, x):
    q.put(x**2)


def main():
    q = Queue()
    p1 = Process(target=square, args=(q, 25))
    p2 = Process(target=square, args=(q, 10))
    p1.start()
    p2.start()
    print(q.get())
    print(q.get())
    p1.join()
    p2.join()

if __name__ == '__main__': 
    main()
 