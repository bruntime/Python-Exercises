# Program Name: Swap Letter Case
# Task Description: Swap the case of each character
# Parameter: Let numbers and symbols stay the way they are. 
# Example: For "Hello World" the output should be hELLO wORLD.

def SwapCase(txt):

	sentence = list(txt)

	swapped_letters = []
	
	a = -1
	
	while a < 20:
		a += 1
		if sentence[a].isupper():
			swapped_letters += [sentence[a].lower()]
		else:
			swapped_letters += [sentence[a].upper()]
	
	sentence = "".join(x for x in swapped_letters)
	
	print sentence
       
user_txt = raw_input("Sentence: ")
SwapCase(user_txt)

#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Swap%20Case&lan=Python