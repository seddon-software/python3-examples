from Setup import *


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('users_seq', start=1000), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    addresses = relationship("Address", backref='myUser', cascade="all, delete, delete-orphan")

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, Sequence('address_seq', start=1000), primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref('myAddresses', order_by=id))

    def __init__(self, email_address):
        self.email_address = email_address
    
    def __repr__(self):
        return "<Address('%s')>" % self.email_address

Base.metadata.create_all(engine) 

1
