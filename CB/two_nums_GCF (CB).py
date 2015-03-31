# Return the greatest number that evenly goes into two numbers with no remainder. 
# For example: 12 and 16 both are divisible by 1, 2, and 4 so the output should be 4. 
# The range for both parameters will be from 1 to 10^3. 

def Division (num1, num2):
	
	a = 0
	b = 0
	
	num1_GCF = []
	num2_GCF = []
	
	while a < num1 + 1:
		a += 1
		if num1 % a == 0:
			num1_GCF.append(a)
		while b < num2 + 1:
			b += 1
			if num2 % b == 0:
				num2_GCF.append(b)	
	print "GCF's for number 1:", num1_GCF, "\nGCF's for number 2:", num2_GCF
	
	common_GCF = []
	
	for x in num1_GCF:
		for y in num2_GCF:
			if x == y:
				common_GCF.append(x)
	print "Greatest Common Factor:", common_GCF[-1]
	
user_num1 = int(raw_input("Number 1: "))
user_num2 = int(raw_input("Number 2: "))

Division(user_num1, user_num2)