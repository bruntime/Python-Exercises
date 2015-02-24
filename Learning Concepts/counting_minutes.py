# count time between two times
# return the total number of minutes between the times

first_hour = int(raw_input("First Hour: "))
first_minute = int(raw_input("First Minutes: "))
second_hour = int(raw_input("Second Hour: "))
second_minute = int(raw_input("Second Minutes: "))
total_hour = second_hour - first_hour
total_minute = second_minute - first_minute
		
if first_hour < 25 and first_minute < 60:
	if second_hour < 25 and second_minute < 60:		
		print "Time between two times: %d:%d" %(total_hour, total_minute)
		#return total number of minutes between the times
else:
	print "invalid time"


