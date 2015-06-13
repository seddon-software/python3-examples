#!/usr/bin/env python

start_string = "01-result.xls,2-result.xls,03-result.xls,05-result.xls"

# Start by splitting the string into a list
str_list = start_string.split(",")

new_list = []
# Loop through the elements and transform the name
for test_name in str_list:
    # Remove the extension
    test_name = test_name.replace('.xls',  '')
    # Split on the dash
    parts = test_name.split('-')
    
    # Turn the number into an Int (to removethe leading 0)
    test_number = int(parts[0])
    
    new_name = parts[1] + str(test_number)
    new_list.append(new_name)

print new_list
