# Program Name: Swap Letter Case
# Task Description: Swap the case of each character
# Parameter: Let numbers and symbols stay the way they are. 
# Example: For "Hello World" the output should be hELLO wORLD.

def SwapCase(txt):

	sentence = list(txt)

	swapped_letters = []
	
	for x in sentence:
		if x.isupper():
			swapped_letters += [x.lower()]
		else:
			swapped_letters += [x.upper()]
	
	sentence = "".join(x for x in swapped_letters)
	
	print sentence
       
user_txt = raw_input("Sentence: ")
SwapCase(user_txt)

#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Swap%20Case&lan=Python