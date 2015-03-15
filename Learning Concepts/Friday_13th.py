#in honor of Friday, 13 March 2015, program will check if date is Friday the 13th

import datetime

# month = int(raw_input("Give a month: "))
year = int(raw_input("Give a year: "))

days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = 0

while month <= 12:
	month += 1
	date = days_of_week[datetime.date(year, (month+1), 13).weekday()]
	print date

if date == "Fri":
	print "Friday the 13th"
else:
	print "Not Friday the 13th"

#next challenge: print all Friday the 13ths in a given year/time period