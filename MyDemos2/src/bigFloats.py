# import decimal
from decimal import *

getcontext().prec = 50

x = Decimal(10.0) / Decimal(7.0)
print x
