from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# cx_oracle must be installed to use Oracle XE

Base = declarative_base()

#engine = create_engine('sqlite:///:memory:', echo=True)
oracleXE = "oracle://java:oracle@localhost:1521/XE"
engine = create_engine(oracleXE)
engine.echo = True
metadata = MetaData(engine)

