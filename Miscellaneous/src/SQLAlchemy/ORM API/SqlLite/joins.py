from setup import *

q = session.query(User, Salary)

for user, salary in q.filter(User.fullname == Salary.fullname). \
                      filter(Salary.salary > 55000).            \
                      all():
    print user.name, salary.salary

session.close()



