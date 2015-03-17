from setup import *

q1 = session.query(User)
q2 = session.query(Salary)

for user in q1.all():
    print user
print

for salary in q2.all():
    print salary
print

