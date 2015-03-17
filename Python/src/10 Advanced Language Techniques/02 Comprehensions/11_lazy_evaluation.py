
import time
print "start" 

# this takes 10 seconds to evaluate - each expression is evaluated
print ["no sleep", time.sleep(5), time.sleep(5)][0]
print "list DONE"
 
# lambdas are not evaluated until called - lazy evaution
print [lambda: "no sleep", lambda: time.sleep(1), lambda: time.sleep(2)][0]()
print "lambdas DONE"

# generator comprehensions are evaluated in a lazy way
z = (time.sleep(n) for n in [0, 5, 5])
z.next()
print "generator comprehension DONE"

# list comprehensions are evaluated immediately - takes 10 seconds
z = [time.sleep(n) for n in [0, 5, 5]] [0]
print "list comprehension DONE"

