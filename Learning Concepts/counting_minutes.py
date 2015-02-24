# count time between two times
# return the total number of minutes between the times

first_hour = int(raw_input("First Hour: "))
first_minute = int(raw_input("First Minutes: "))
second_hour = int(raw_input("Second Hour: "))
second_minute = int(raw_input("Second Minutes: "))
total_hour = second_hour - first_hour
hour_to_minutes = total_hour * 60
total_minute = (second_minute - first_minute) + hour_to_minutes
		
if first_hour < 25 and first_minute < 60:
	if second_hour < 25 and second_minute < 60:		
		print "Total minutes:%d minutes" %(total_minute)
		#return total number of minutes between the times
else:
	print "invalid time"


