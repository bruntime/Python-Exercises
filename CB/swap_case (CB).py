# Program Name: Swap Letter Case
# Task Description: Swap the case of each character
# Parameter: Let numbers and symbols stay the way they are. 
# Example: For "Hello World" the output should be hELLO wORLD.

def SwapCase(sentence):
   
    uppercase = [x for x in sentence if x.isupper()]
    lowercase = [x for x in sentence if x.islower()]

    for x in uppercase:
        print x.lower()
    for x in lowercase:
        print x.upper()
       
user_txt = raw_input("Sentence: ")
SwapCase(user_txt)