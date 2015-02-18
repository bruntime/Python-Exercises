#Temperature Converter

def fromFahrenheit(num, choice):

	if choice == 'Celsius':
		to_celsius = (num - 32) * 5/9
		print "Temperature: %d F has been converted to %d C" %(num, to_celsius)
	if choice == 'Kelvin':
		to_kelvin = (num + 459.67) * 5/9
		print "Temperature: %d F has been converted to %d K" %(num, to_kelvin)
	if choice == 'Rankine':
		to_rankine = num + 459.67
		print "Temperature: %d F has been converted to %d K" %(num, to_rankine)
	if choice == 'Fahrenheit':
		print "Temperature is already in Fahrenheit"
	# else:
		# print "This is not a valid type"

# functions for other temperature types		
		
# def fromCelsius():
# def fromKelvin():
# def fromRankine()		
		
user_num = int(raw_input("Temperature: "))
current_type = raw_input("Current temperature type (Fahrenheit, Celsius, Kelvin, Rankine): ")
temp_choice = raw_input("Converting to which? Fahrenheit, Celsius, Kelvin, Rankine: ")

if current_type == "Fahrenheit":
	fromFahrenheit(user_num, temp_choice)
if current_type == "Celsius":
	fromCelsius(user_num, temp_choice)
if current_type == "Kelvin":
	fromKelvin(user_num, temp_choice)
if current_type == "Rankine":
	fromRankine(user_num, temp_choice)




