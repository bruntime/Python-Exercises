#in honor of Friday, 13 March 2015, program will check if date is Friday the 13th

import datetime

days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

attempt = raw_input("Would you like to give a year? (Y or N): ")

month = 0

while attempt == 'Y' or attempt == 'y':
	year = int(raw_input("Give a year: "))
	while month <= 11:
		month += 1
		date = days_of_week[datetime.date(year, (month), 13).weekday()]
		if date == "Fri":
			print datetime.date(year, (month), 13), "FRIDAY THE 13TH"
		else:
			print datetime.date(year, (month), 13)
			
#next challenge: print all Friday the 13ths in a given year/time period