# Program Name: Reverse Word Order
# Task Description: Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# Parameter: N/A
#Example: "My name is Michele" prints "Michele is name My"

user_txt = raw_input("Sentence: ")
reversed_txt = user_txt.split()

print reversed_txt[::-1]
		
#http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html