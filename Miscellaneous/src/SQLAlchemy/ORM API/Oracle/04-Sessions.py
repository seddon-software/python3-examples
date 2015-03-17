from Setup import *
from ORMClasses import *

try:
    Session = sessionmaker(bind=engine)
    session = Session()

    for u in session.query(User):   
        print u
        session.delete(u)
    session.commit()

    ted = User('Edward', 'Jones', 'edspassword')
    session.add(ted)
    our_user = session.query(User).filter_by(name='Edward').first()
    print our_user
    ted.password = 'f8s7ccs'
    print session.dirty
    session.commit()

    ted.password = 'z3ewqe46'
    print session.dirty
    session.rollback()
    our_user = session.query(User).filter_by(name='Edward').first()
    print our_user

    session.add_all([
        User('Wendy', 'Williams', 'foobar'),
        User('Mary', 'Contrary', 'xxg527'),
        User('Fred', 'Flintstone', 'blah')])
    print session.new
    session.commit()
except Exception, e:
    print e
    session.rollback()



1
