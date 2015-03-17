from setup import *

q1 = session.query(User)
q2 = session.query(Salary)
print q1.filter_by(name='bill').first()
print q1.filter_by(name='seb').first()
print q2.filter_by(fullname='Jo Lyon').first()
print q2.filter_by(fullname='Jane Doe').first()

