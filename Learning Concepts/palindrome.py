# Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

def Palindrome(str):

	if str == str.reverse():
		return "true"
	else:
		return "false"

txt = raw_input("Test if palindrome: ")		

Palindrome(txt)

# http://www.coderbyte.com/CodingArea/Editor.php?ct=Palindrome&lan=Python

