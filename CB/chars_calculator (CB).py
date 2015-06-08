# Program Name: Calculator
# Task Description: Take the str parameter being passed and evaluate the mathematical expression within in.
# Parameter: There can be parenthesis within the string so you must evaluate it properly according to the rules of arithmetic. The string will contain the operators: +, -, /, *, (, and ). If you have a string like this: #/#*# or #+#(#)/#, then evaluate from left to right. So divide then multiply, and for the second one multiply, divide, then add. The evaluations will be such that there will not be any decimal operations, so you do not need to account for rounding.
# Example: If str were "2+(3-1)*3" the output should be 8. Another example: if str were "(2-0)(6/2)" the output should be 6.

def calculator(str):

	chars = ['+', '-', '/', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9' '0']
	txt_char = [] #characters from string
	
	for x in str:
		for y in chars:
			if x == y:
				txt_char = txt_char + [y]
	
	print txt_char

user_txt = raw_input("text: ")
calculator(user_txt)

#http://coderbyte.com/CodingArea/Editor.php?ct=Calculator&lan=Python