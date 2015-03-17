from Setup import *
from ORMClasses import *

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    for u, a in session.query(User, Address).\
            filter(User.id == Address.user_id).\
            filter(Address.email_address=='jack@google.com').\
            all():
        print u, a
except Exception, e:
    print e


1
