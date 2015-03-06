# So today let us do some calendar math. Given a date that is in the future how many days until that date from the current date?

#Example Input: 2015 2 14
#Example Output: 5 days from 2015 2 9 to 2015 2 14

from datetime import date

print "First Date"
first_month = int(raw_input("Month (1-12 i.e. January = 1, February = 2, etc.): "))
first_day = int(raw_input("Day: "))
first_year = int(raw_input("Year: "))

print "Second Date"
second_month = int(raw_input("Month (1-12 i.e. January = 1, February = 2, etc.): "))
second_day = int(raw_input("Day: "))
second_year = int(raw_input("Year: "))

first_date = date(first_year, first_month, first_day)
second_date = date(second_year, second_month, second_day)

total = first_date - second_date

print "%d days from %s to %s" %(total.days, first_date, second_date)

#http://www.reddit.com/r/dailyprogrammer/comments/2vc5xq/20150209_challenge_201_easy_counting_the_days/