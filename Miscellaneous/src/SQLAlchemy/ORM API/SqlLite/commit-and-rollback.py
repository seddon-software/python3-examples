from setup import *

def printTable(query):
    for user in q.all():
        print user
    print
    
session.commit()

q = session.query(User)
printTable(q)

user1 = User(name='pete', fullname='Pete Swan', password='petespassword')
user2 = User(name='adil', fullname='Adil Qureshi', password='adilspassword')
session.add_all([user1, user2])
session.commit()

q = session.query(User)
printTable(q)


user1 = User(name='faker1', fullname='Jim Faker', password='faker')
user2 = User(name='faker2', fullname='Sue Faker', password='faker')
session.add_all([user1, user2])
session.rollback()

q = session.query(User)
printTable(q)




