from multiprocessing import Process

def square(x):
    print(x**2)

# required for Windows
if __name__ == '__main__':
    p = Process(target=square, args=(25,))
    p.start()
    p.join()
    