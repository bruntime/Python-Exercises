#Water Prepping Calculator

water_gallon = 30

print "1 Person needs", water_gallon, " gallons of water to survive for 1 month"

mths_of_survival = int(raw_input("How many months will you need to survive? "))

person = int(raw_input("How many people will need water? "))

total_water_need = person * (mths_of_survival * water_gallon)

current_water_total = int(raw_input("How much water do you have? "))
water_missing = total_water_need - current_water_total

if water_missing < 0:
	print "You have MORE than enough water to survive %d months of a disaster" % (mths_of_survival)
elif water_missing == 0:
	print "You have just enough water to last you %d months during the apocalypse" %(mths_of_survival)
else:
	print "I'm not sure you'll make it. You need %d more gallons of water." %(water_missing)