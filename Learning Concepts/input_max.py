#Description: accept strings as input until there are 15 strings accepted or user input is empty 

#If input contains digits (0 -9) display the sum of digits and ignore the other characters
#If input is palindrome display the string "palindrome", otherwise print the input in reverse order (case sensitive)

txt = []
user_txt = raw_input("Text: ")

while len(txt) != 15:
	txt = txt + [user_txt]
	if user_txt == "":
		break

print txt
print len(txt)