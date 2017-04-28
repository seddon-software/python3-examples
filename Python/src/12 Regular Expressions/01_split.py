#######################################################
#
#       split
#
#######################################################

import re

pattern = re.compile(r"[\s^;]+")
text = "  aaa  ; bbb ;ccc     ;    ^    ddd ;  eee   "
mylist = pattern.split(text.strip())
print(mylist)
1