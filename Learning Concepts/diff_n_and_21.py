#Exercise: Difference between n and 21

def diff_between(n):

	difference = abs(21 - n)
	
	if n > 21:
		print difference * 2
	else:
		print difference
		
txt = int(raw_input("Give me a number: "))
	
diff_between(txt)