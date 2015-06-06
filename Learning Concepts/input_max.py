#Check user input for: 1) max 15 strings, 2) user input empty, 3) contains digits, 4) palindrome
#If input contains digits (0 -9) display the sum of digits and ignore the other characters
#If input is palindrome display the string "palindrome", otherwise print the input in reverse order (case sensitive)

def check_digits(str):

	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	txt = list(str)
	numbers_in_txt = [] #list for numbers in user input
	
	for x in txt:
		for y in numbers:
			if x == y in numbers:
				numbers_in_txt.append(int(x))
				
	if len(numbers_in_txt) > 0:
		print sum(numbers_in_txt)
	numbers_in_txt = []
	
def check_palindrome(str):
			
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	
	letters = str.replace(" ", "")
	reversed_txt = letters[::-1]
	
	for x in numbers:
		if x in letters:
			return
	
	if letters.lower() == reversed_txt.lower():
		print 'palindrome'
	else:
		print reversed_txt

count = 0

while count <= 14:
	count += 1
	user_txt = raw_input("Type here: ")
	print user_txt
	if check_digits(user_txt):
		print "check", user_txt
	elif check_palindrome(user_txt):
		print user_txt
	elif user_txt == "":
		count -= 1
		break
		
print "There were",  count, "input(s)"