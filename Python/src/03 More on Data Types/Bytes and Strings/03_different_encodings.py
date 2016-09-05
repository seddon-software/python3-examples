#!/usr/bin/env python
# -*- coding: latin-1 -*-

# the second line of this script defines the default unicode encoding (normally UTF-8)

# find code point for last character in string
u = 'abcdé'
print(u)
print(ord(u[-1]))

# convert to bytes
b = u.encode('latin1')
print(b)
