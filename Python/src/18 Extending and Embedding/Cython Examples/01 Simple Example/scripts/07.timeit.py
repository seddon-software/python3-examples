def doTimings():
    t1 = Timings(title = "cython", setup = "import os, hello",
                                   statement = "hello.fibonacci(100)")
    t2 = Timings(title = "python", setup = ("import os, sys"            "\n"
                                            "sys.path.append('../src')" "\n"
                                            "import _hello"             "\n"
                                           ), 
                                   statement = "_hello.fibonacci(100)")
    u1 = Timings(title = "cython", setup = "import os, hello",
                                   statement = "hello.sumOfSquares(1000, 4000000)")
    u2 = Timings(title = "python", setup = ("import os, sys"            "\n"
                                            "sys.path.append('../src')" "\n"
                                            "import _hello"             "\n"
                                           ), 
                                   statement = "_hello.sumOfSquares(1000, 4000000)")
    
    Timings.titles()
    t1.run(1000000)
    t2.run(1000000)
    u1.run(20)
    u2.run(20)


#####################################################
# code to make timings table
import timeit
class Timings(timeit.Timer):
    def __init__(self, title, setup, statement):
        self.title = title
        self.timer = timeit.Timer(stmt = statement, setup = setup)
    def run(self, number):
        t = self.timer.timeit(number=number)
        print "{:20s}{:8d}{:8.3f}{:8.3f}".format(self.title, number, t, 1/t)

    @staticmethod
    def titles():
        print "{:20s}{:>8s}{:>8s}{:>8s}".format("code", "runs", "time", "1/time")
        print "{:20s}{:>8s}{:>8s}{:>8s}".format("====", "====", "====", "======")


doTimings()


