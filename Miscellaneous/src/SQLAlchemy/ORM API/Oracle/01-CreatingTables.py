from Setup import *
from ORMClasses import *

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    jack = User('Jack', 'Smith', 'gjffdd')
    jack.addresses = [
                 Address(email_address='jack@google.com'),
                 Address(email_address='jack253@yahoo.com')]
    
    mary = User('Mary', 'Taylor', 'secret')
    mary.addresses = [
                 Address(email_address='mary55@hotmail.com'),
                 Address(email_address='mary565@yahoo.com')]
    session.add(jack)
    session.add(mary)
    session.commit()
except Exception, e:
    print e


1
