import pandas as pd
import numpy as np

def title(t):
    print "\n"
    print t
    print "=" * len(t)

pd.set_option('display.width', 1000)
pd.set_option('display.precision', 2)

##########
title("create a series")
s = pd.Series(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], index=['A', 'B', 'C', 'D', 'E'])
print s

##########
title("create a series from a dict")
d = { "john"  : 34000, 
      "sara"  : 27000,
      "pedro" : 52000,
      "tim"   : None,
      "zoe"   : 66000 }

salaries = pd.Series(d)
print salaries

##########
title("select from series")
print salaries[["sara", "pedro", "zoe"]]
print salaries.john
print salaries[salaries < 40000]

##########
title("modifying series")
print 'Old value:', salaries['tim']
salaries['tim'] = 41000
print 'New value:', salaries['tim']

##########
title("modifying series using predicates")
# changing values using boolean logic
salaries[salaries < 45000] = 25000
print salaries[salaries < 26000]

##########
title("check if item present in series")
print 'john' in salaries
print 'mary' in salaries

##########
title("perform operations on series")
# divide salaries values by 3
print salaries / 3

##########
title("add series together")
s1 = salaries[['john', 'pedro']]
s2 = salaries[['zoe']]
s = s1 + s2
print s

##########
title("check for nulls in series")
salaries['mary'] = None
salaries.notnull()
print salaries.isnull()
print salaries[salaries.isnull()]
