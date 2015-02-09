# Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

import sys

def Palindrome(str):

	str = None

	#if str == str.reverse(): #this does not work because Python does not have a built-in reverse function for Strings
	# new_str = str.split( )
	# new_str = (reverse(str))
	# new_str = join(reverse(str))
	if str == new_str:
		return "true"
	else:
		return "false"

txt = raw_input("Test if palindrome: ")		

new_txt = txt.split()
txt_reverse = new_txt.reverse()
print txt_reverse #message: None - not expected outcome

# Palindrome(txt)

# http://www.coderbyte.com/CodingArea/Editor.php?ct=Palindrome&lan=Python

