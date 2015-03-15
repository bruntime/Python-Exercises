#in honor of Friday, 13 March 2015, program will check if date is Friday the 13th

import datetime

# month = int(raw_input("Give a month: "))

days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month = 0

attempt = raw_input("Would you like to give a year?: ")
	while attempt == 'Y' or attempt == 'y':
		year = int(raw_input("Give a year: "))
		while year < 5000:
			while month <= 11:
				month += 1
				date = days_of_week[datetime.date(year, (month), 13).weekday()]
			if date == "Fri":
				print datetime.date(year, (month), 13), "FRIDAY THE 13TH"
			else:
				print datetime.date(year, (month), 13)
		break
#next challenge: print all Friday the 13ths in a given year/time period