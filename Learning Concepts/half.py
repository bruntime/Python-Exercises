#Divide number by two to make a new number.

#example: 100, the screen output should be - 100, 50, 25, 12.5 ....

def half(num):

    while num > 0:
      divide_two = num / 2
      print divide_two


user_num = raw_input("number: ")
half(user_num)