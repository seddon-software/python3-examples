import random, time

def main():
    work_with_generators(10, 5.0)
    work_with_lists(10, 5.0)
                        
def delay(T):
    time.sleep(random.random() * T)   # random delay
    
def work_with_generators(N, T):
    print "work with generators"

    # this generator simulates data arriving at random intervals
    def producer():
        data = (n for n in range(N))
        while True:
            yield data.next()
            delay(T)
    
    # consume the data
    g = producer()
    for n in range(10):
        print g.next(),
    print

def work_with_lists(N, T):
    print "work with lists"

    # simulate waiting for all the data to arrive before consuming
    def producer():
        for i in range(N):
            delay(T)
        return range(N)
    
    # consume the data
    g = producer()
    for n in range(N):
        print g[n],
    print

main()
