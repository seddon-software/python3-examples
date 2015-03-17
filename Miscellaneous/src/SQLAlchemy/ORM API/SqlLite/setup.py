import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper




engine = create_engine('sqlite:///:memory:', echo=False)


metadata = MetaData()

users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('password', String)
    )

salary_table = Table('salary', metadata,
    Column('id', Integer, primary_key=True),
    Column('fullname', String),
    Column('salary', Integer)
    )

metadata.create_all(engine) 

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s', '%s')>" % (self.id, self.name, self.fullname, self.password)

class Salary(object):
    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.salary = salary

    def __repr__(self):
        return "<Salary('%s','%s','%s')>" % (self.id, self.fullname, self.salary)
    
mapper(User, users_table) 
mapper(Salary, salary_table) 

user1 = User(name='ed',   fullname='Ed Jones',   password='edspassword')
user2 = User(name='jo',   fullname='Jo Lyon',    password='jospassword')
user3 = User(name='bill', fullname='Bill Pane',  password='billspassword')
user4 = User(name='seb',  fullname='Seb Frith',  password='sebspassword')
user5 = User(name='bill', fullname='Bill Smith', password='billsspassword')

salary1 = Salary(fullname='Ed Jones',   salary=52000)
salary2 = Salary(fullname='Jo Lyon',    salary=58000)
salary3 = Salary(fullname='Bill Pane',  salary=32000)
salary4 = Salary(fullname='Seb Frith',  salary=79000)
salary5 = Salary(fullname='Bill Smith', salary=61000)

myObjects = [user1, user2, user3, user4, user5, 
             salary1, salary2, salary3, salary4, salary5]

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add_all(myObjects)

