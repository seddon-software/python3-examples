"""
Write a program that inputs a 4 digit year and then 
calculates whether or not it is a leap year.
"""

def isLeap(year):
    result = False
    if year %   4 == 0: result = True
    if year % 100 == 0: result = False
    if year % 400 == 0: result = True
    return result


year = int(raw_input("Enter a year: "))

if isLeap(year):
    print str(year) + " is a leap year"
else:
    print str(year) + " is NOT a leap year"

1