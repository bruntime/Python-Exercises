# Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

import sys

def is_palindrome(txt):

	if txt == reversed(txt):
		print "It's a palindrome"
	else:
		print "This is not a palindrome"

user_txt = raw_input("Enter a palindrome: ")

is_palindrome(user_txt)

# http://www.coderbyte.com/CodingArea/Editor.php?ct=Palindrome&lan=Python

