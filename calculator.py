#Water Prepping Calculator for 1 Month

water_gallon = 30
months = 1

print "1 Person needs", water_gallon, " gallons of water to survive for 1 month"

water_amt = int(raw_input("How much water do you have? "))
water_total = (months * water_gallon) - water_amt

if water_total > 0:
	print "You do not have enough water. You need %d more gallons of water" % (water_total)
else:
	print "You have more than enough water"