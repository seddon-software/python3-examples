from Setup import *
from sqlalchemy.sql import update

try:    
    connection = engine.connect()
    users = Table('users', metadata, autoload=True)
    statement = update(users).where(users.c.name=="Adil").values(age=37)
    connection.execute(statement)
    connection.close()
    
except Exception, e:
    print e


1
