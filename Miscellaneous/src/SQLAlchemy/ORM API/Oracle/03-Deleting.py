from Setup import *
from ORMClasses import *

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    for u in session.query(User).\
            filter(User.addresses.any(Address.email_address.like('%google%'))):   
        print u
        session.delete(u)
    session.commit()
except Exception, e:
    print e
    session.rollback()


1
