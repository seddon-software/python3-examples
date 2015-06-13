#!/usr/bin/env python

# Get the IP Address
addr = raw_input("Enter an IP Address: ")

# Find the position of the first point
first_point = addr.find('.')
# Extract the  first quad from the string
first_quad = addr[0:first_point]

# Need to add one to the position to move the start  past the '.'
second_point = addr.find('.', first_point+1)
second_quad = addr[first_point+1:second_point]

third_point = addr.find('.', second_point+1)
third_quad = addr[second_point+1:third_point]

# The last quad is from the third point to the end of the string
fourth_quad = addr[third_point+1:]

print "The address elements are: {} {} {} {}".format(first_quad,  second_quad,  third_quad,  fourth_quad)

