# Program Name: Coin Determiner
# Task Description: Take integers and return an integer output that will specify the least number of coins, that when added, equal the input integer.
# Parameter: Integers range from 1 to 250, coins representing the integers 1, 5, 7, 9, and 11.
# Example: If num is 16, then the output should be 2 because you can achieve the number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins. 

from itertools import combinations

def coin_combinations (num):

	coins = [1, 5, 7, 9, 11]

	coin_combo = sum([map(list, combinations(coins, i)) for i in range(len(coins) + 1)], [])

	count = 0

	for x in coin_combo:
		if sum(x) == num:
			count += 1
			print x

	print count

user_txt = int(raw_input("Number (between 1 - 25): "))
coin_combinations(user_txt)