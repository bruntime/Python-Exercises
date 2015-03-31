# have the function SimpleAdding(num) add up all the numbers from 1 to num.

def SimpleAdding(num):

	sum = 0
	
	for i in range(1, num+1):
		sum += i
		print sum

end_num = int(raw_input("Pick a number: "))

SimpleAdding(end_num)

#http://www.coderbyte.com/CodingArea/Editor.php?ct=Simple%20Adding&lan=Python