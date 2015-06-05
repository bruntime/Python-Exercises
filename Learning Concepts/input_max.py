#Check user input for: 1) max 15 strings, 2) user input empty, 3) contains digits, 4) palindrome
#If input contains digits (0 -9) display the sum of digits and ignore the other characters
#If input is palindrome display the string "palindrome", otherwise print the input in reverse order (case sensitive)

#function to check if string contains digits
def check_digits(str):

	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	numbers_in_txt = [] #list for numbers in user input

	for x in str:
		for y in numbers:
			if x == y in numbers:
				numbers_in_txt.append(int(x))
				
	if len(numbers_in_txt) > 0:
		print sum(numbers_in_txt)
	numbers_in_txt = []

txt = [] #list for user input

#accept string until 15 strings accepted or user input is empty
while len(txt) != 15:
	user_txt = raw_input("Test: ")
	txt = txt + [user_txt]
	if user_txt == "":
		txt.pop()
		break

count = -1

for x in txt:
	count += 1
	print txt[count]
	if check_digits(x):
		print x

print "There were",  len(txt), "input(s)"