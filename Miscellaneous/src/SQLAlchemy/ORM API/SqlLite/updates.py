from setup import *

def printTable(query):
    for user in query.all():
        print user
    print

q1 = session.query(User)
q2 = session.query(Salary)
printTable(q1)
printTable(q2)



q1 = session.query(User)
q2 = session.query(Salary)

password = {'password':'xyz123'}
salary = {'salary': 81000}
q1.filter(User.fullname == 'Bill Smith').update(password)            
q2.filter(Salary.fullname == 'Seb Frith').update(salary)            
session.commit()

q1 = session.query(User)
q2 = session.query(Salary)
printTable(q1)
printTable(q2)

user1.name = 'edward'
user1.fullname = 'Edward Jones'
session.commit()
q1 = session.query(User)
printTable(q1)


