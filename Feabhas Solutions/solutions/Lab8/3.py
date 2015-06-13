#!/usr/bin/env python

max_val = raw_input("Enter the Max Value: ")

val_range = range(int(max_val))

for test_val in val_range:
    if (test_val == 0):
        odd_even = "Zero"
    elif (test_val % 2 == 0):
        odd_even = "Even"
    elif(test_val % 2 == 1):
        odd_even = "Odd"
    else:
        odd_even = "Unknown"

    print "Value {} is {}".format(test_val,  odd_even)
