from Setup import *
from sqlalchemy.sql import select

try:    
    connection = engine.connect()
    users = Table('users', metadata, autoload=True)
    
    statement = select([users])
    result = connection.execute(statement)
    
    for row in result:
        print row

    connection.close()
    
except Exception, e:
    print e


1
