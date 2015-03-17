from sqlalchemy import *
from sqlalchemy.schema import *
# cx_oracle must be installed to use Oracle XE

#engine = create_engine('sqlite:///:memory:', echo=True)
oracleXE = "oracle://java:oracle@localhost:1521/XE"
engine = create_engine(oracleXE)
engine.echo = True
metadata = MetaData(engine)

