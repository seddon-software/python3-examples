from Setup import *

data = (
            dict(name = 'Steve', age = 21, password='passw0rd'),
            dict(name = 'Jim',   age = 23, password='passw1rd'),
            dict(name = 'Peter', age = 31, password='passw2rd'),
            dict(name = 'Zoe',   age = 42, password='passw3rd'),
            dict(name = 'Holga', age = 24, password='passw4rd'),
            dict(name = 'Susan', age = 21, password='passw5rd'),
            dict(name = 'Ann',   age = 22, password='passw6rd'),
            dict(name = 'John',  age = 43, password='passw7rd'),
            dict(name = 'Larry', age = 37, password='passw8rd'),
            dict(name = 'Mary',  age = 28, password='passw9rd'),
            dict(name = 'Adil',  age = 41, password='passw0rd'),
            dict(name = 'Wei',   age = 55, password='passw1rd')
        )
try:    
    connection = engine.connect()
    seq = Sequence("users_seq")
    users = Table('users', metadata, autoload=True)
    
    # set up insert object
    for entry in data:
        entry['user_id'] = engine.execute(seq)
        statement = users.insert(values=entry)
        connection.execute(statement)
        
    connection.close()
    
except Exception, e:
    print e


1
