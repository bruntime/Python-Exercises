# Program Name: Caesar Cipher
# Task Description: Encrypt a message using keys
# Parameter: N/A
# Example: 

#Working through Invent With Python tutorial

import pyperclip

message = raw_input('Message: ')

key = 13 # (de)encryption key

mode = 'encrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ' '

message = message.upper()

for symbol in message:
	if symbol in letters:
		num = LETTERS.find(symbol)
		if mode == 'encrypt':
			num = num + key
		elif mode == 'decrypt':
			num = num - key
		
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0:
			num = num + len(LETTERS)
		
		translated = translated + LETTERS[num]
	else:
		translate = translated + symbol
	
print(translated)

pyperclip.copy(translated)
		
#http://inventwithpython.com/hacking/chapter6.html
