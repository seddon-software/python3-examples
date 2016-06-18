
import time
print "start" 

# this takes 10 seconds to evaluate - each expression is evaluated
print ["no sleep", time.sleep(5), time.sleep(5)][0]
print "list DONE"

# list comprehensions are evaluated immediately - takes 10 seconds
myComprehension = [time.sleep(n) for n in [0, 5, 5]]
myComprehension[0]
print "list comprehension DONE"
 
# generator comprehensions are evaluated in a lazy way
myIterator = (time.sleep(n) for n in [0, 5, 5])
myIterator.next()
myIterator.next()
print "generator comprehension DONE"

# lambdas are not evaluated until called - lazy evaution
myLambdas = [lambda: time.sleep(5), lambda: time.sleep(5), lambda: "no sleep"]
myLambdas[2]()
print "lambdas DONE"



