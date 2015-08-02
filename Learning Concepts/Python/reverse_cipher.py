# Program Name: Reverse Cipher
# Task Description: Encrypt a message by printing it in reverse order
# Parameter: N/A
# Example: "Hello world!" encrypts to "!dlrow olleH"

#Working through Invent With Python tutorial

message = "Two can keep a secret, if one of them is dead."
translated = ' '

i = len(message) - 1

while i >= 0:
	translated = translated + message[i]
	i = i - 1

print(translated)

#http://inventwithpython.com/hacking/chapter5.html
