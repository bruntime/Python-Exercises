def VowelCount(str): 

  
	vowels = ['a', 'e', 'i', 'o', 'u']
  
	count = 0
  
	# for i in vowels:
	if i in vowels:
		for i in str:
			count += 1
    
usertxt = raw_input("Some random text: ")
	
print VowelCount(usertxt)  
