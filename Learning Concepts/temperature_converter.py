#Temperature Converter - Fahrenheit, Celsius, Kelvin, Rankine

def fromFahrenheit(num, choice):

	if choice == 'Fahrenheit':
		print "Temperature is already in Fahrenheit"
	elif choice == 'Celsius':
		to_celsius = (num - 32) * 1.8
		print "Temperature: %d F has been converted to %d C" %(num, to_celsius)
	elif choice == 'Kelvin':
		to_kelvin = (num + 459.67) * 1.8
		print "Temperature: %d F has been converted to %d K" %(num, to_kelvin)
	elif choice == 'Rankine':
		to_rankine = num + 459.67
		print "Temperature: %d F has been converted to %d R" %(num, to_rankine)
	else:
		print "This is not a valid type"
		
def fromCelsius(num, choice):

	if choice == 'Celsius':
		print "Temperature is already in Celsius"
	elif choice == 'Fahrenheit':
		to_fahrenheit = (num * 1.8) + 32
		print "Temperature: %d C has been converted to %d F" %(num, to_fahrenheit)
	elif choice == 'Kelvin':
		to_kelvin = num + 273.15
		print "Temperature: %d C has been converted to %d K" %(num, to_kelvin)
	elif choice == 'Rankine':
		to_rankine = num + 273.15 * 1.8
		print "Temperature: %d C has been converted to %d R" %(num, to_rankine)
	else:
		print "This is not a valid type"

def fromKelvin(num, choice):
	
	if choice == 'Kelvin':
		print "Temperature is already in Kelvin"
	elif choice == 'Fahrenheit':
		to_fahrenheit = (num * 1.8) - 459.67
		print "Temperature: %d K has been converted to %d F" %(num, to_fahrenheit)
	elif choice == 'Celsius':
		to_celsius = num - 273.15
		print "Temperature: %d K has been converted to %d C" %(num, to_celsius)
	elif choice == 'Rankine':
		to_rankine = num * 1.8
		print "Temperature: %d K has been converted to %d R" %(num, to_rankine)
	else:
		print "This is not a valid type"

def fromRankine(num, choice):		
		
	if choice == 'Rankine':
		print "Temperature is already in Rankine"
	elif choice == 'Fahrenheit':
		to_fahrenheit = num - 459.67
		print "Temperature: %d R has been converted to %d F" %(num, to_fahrenheit)
	elif choice == 'Celsius':
		to_celsius = (num - 491.67) * 1.8
		print "Temperature: %d R has been converted to %d C" %(num, to_celsius)
	elif choice == 'Kelvin':
		to_rankine = num * 1.8
		print "Temperature: %d R has been converted to %d K" %(num, to_kelvin)		
	else:
		print "This is not a valid type"
		
user_num = int(raw_input("Temperature: "))
current_type = raw_input("Current temperature type (Fahrenheit, Celsius, Kelvin, Rankine): ")
temp_choice = raw_input("Converting to which? Fahrenheit, Celsius, Kelvin, Rankine: ")

if current_type == "Fahrenheit":
	fromFahrenheit(user_num, temp_choice)
elif current_type == "Celsius":
	fromCelsius(user_num, temp_choice)
elif current_type == "Kelvin":
	fromKelvin(user_num, temp_choice)
elif current_type == "Rankine":
	fromRankine(user_num, temp_choice)
else:
	print "Your current temperature type is not valid"




