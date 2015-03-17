from Setup import *
from sqlalchemy.sql import delete

try:    
    connection = engine.connect()
    users = Table('users', metadata, autoload=True)
    statement = delete(users).where(users.c.name=="Wei")
    connection.execute(statement)
    connection.close()
    
except Exception, e:
    print e

1
