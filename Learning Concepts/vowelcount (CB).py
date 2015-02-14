def VowelCount(str): 
  
	vowels = ['a', 'e', 'i', 'o', 'u']
  
	count = 0

	for vowels in vowels:
		if vowels in str:
			count += 1
	
usertxt = raw_input("Some random text: ")
	
print VowelCount(usertxt)  
