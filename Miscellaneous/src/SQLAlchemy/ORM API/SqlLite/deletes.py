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

q1.filter(User.name == 'jo').delete()
q2.filter(Salary.fullname == 'Jo Lyon').delete()
            
session.commit()

q1 = session.query(User)
q2 = session.query(Salary)
printTable(q1)
printTable(q2)

