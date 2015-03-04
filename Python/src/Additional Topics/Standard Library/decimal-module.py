############################################################
#
#    Decimals
#
############################################################

# from decimal import *
# 
# x = 1
# for n in range(1, 500):
#     x = x * n
# 
# print x
#     
# getcontext().prec = 1000
# x = Decimal("1.0") / Decimal("7.0")
# 
# print x


    
    
############################################################
#
#    Decimals
#
############################################################

from decimal import *

# factorial
x = 1
for n in range(1, 500):
    x = x * n
print x


getcontext().prec = 1000
x = Decimal("1.0") / Decimal("7.0")
y = Decimal("1.0").exp()
print x
print y

ctx = Context(prec = 60, rounding = ROUND_UP)

z = Decimal("1.0").exp(ctx)
print z




    
    
