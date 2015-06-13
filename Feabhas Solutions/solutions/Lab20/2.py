#!/usr/bin/env python

import argparse
import datetime
import sys

ERR_DATE_ENTERED = 1
ERR_DATE_FMT = 2
ERR_DATE_PARSE = 3

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--date",  help="date to check (YYYY-MM-DD)", default=datetime.datetime.today().isoformat(),  type=str)
args = parser.parse_args()

dates = args.date.split('-')

# Split the date
try:
    year = int(dates[0])
    month = int(dates[1])
    # In case we have a full ISO format date...
    tmp = dates[2].split('T')    
    day = int(tmp[0])
except (IndexError,  ValueError) as ex:
    print "Invalid Date"
    sys.exit(ERR_DATE_ENTERED)
    
# Next check - did the user read the manual?
if (year < 32):
    # While this puts a minimumm year we can check, at does provide one sanity check
    print "Please enter the date in the format YYYY-MM-DD"
    sys.exit(ERR_DATE_FMT)

try:
    start_date = datetime.datetime(year=year,  month=month,  day=day)
except ValueError as ex:
    print "Invalid Date"
    sys.exit(ERR_DATE_PARSE)

# Check if the start date is after christmas
if (month == 12 and day > 25):
    # In which case we want *next* christmas
    year += 1
    
christmas = datetime.datetime(year=year,  month=12,  day=25)

delta_til_christmas = christmas - start_date

if (delta_til_christmas.days  == 0):
    print "IT's CHRISTMAS!"
else:
    print "There are {} days until christmas".format(delta_til_christmas.days)
