#######################################################
#
#       split
#
#######################################################

import re

pattern = re.compile(r"[\s^;]+")
text = "  aaa  ; bbb ;ccc     ;    ^    ddd ;  eee   "
list = pattern.split(text.strip())
print list
1