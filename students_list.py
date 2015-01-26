#Create a list that contains the names of 5 students of this class

#NOTE: the last comma in list is not considered an error in Python
class_students = ['Candace Gordie', 'Wesley Baise', 'Max Lexington', 'Samantha Who', 'Xho Zu', ] 			

student_add = raw_input("Add a student - first and last name: ")

#students added to beginning of list
class_students = [student_add] + class_students

#students added to end of list
student_add = raw_input("Add another student: ")
class_students.append(student_add)

for x in class_students:
	print x
	
class_students = ['John Smith', 'Mary Miller'] + class_students
	
class_students.sort()
print "alphabetical order:", class_students

student_num = input("Please input a number between 0 - 8: ")
x = student_num
print class_students[x]

#removes last element in list
del class_students[-1]
print class_students