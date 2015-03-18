#in honor of Friday, 13 March 2015, program will check if date is Friday the 13th

import datetime

def check_Fri_13th(user_year):

	days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

	month = 0

	while month <= 11:
		month += 1
		date = days_of_week[datetime.date(user_year, (month), 13).weekday()]
		if date == "Fri":
			print datetime.date(user_year, (month), 13), "FRIDAY THE 13TH"
		else:
			print datetime.date(user_year, (month), 13)

attempt = int(raw_input("How many times would you like to check year? "))
count = 0

while count <= attempt:
	count += 1
	year = int(raw_input("Give a year: "))
	check_Fri_13th(year)