import random as ran
import time as t

def win(number_of_matches, number):
	global balance
	global placed_bet
	print("Congrats! You got", number_of_matches, "of the same number!")
	reward = (numbers[number][1] * number_of_matches) * placed_bet
	print("You won", reward, "tokens!")
	balance += reward

#Signifies each items chance and reward
numbers = {1: [10000, 1], 2: [7000, 2], 3: [6000, 3], 4: [5000, 4], 5: [4000, 5], 6: [3000, 6], 7: [2000, 10], 8: [1000, 20], 9: [500, 100], 10: [1, 10000]}
weighted_numbers = [number for number in numbers for i in range (numbers[number][0])]

print("Welcome! It costs 1 token to play")
balance = 10

print("Your remaining balance is", balance)

#Main gambling function
while True:
	#Prevents betting with no tokens
	if balance <= 0:
		print("Sorry, but you dont have any more money to gamble with. Hopefully you can come again sometime!")
		break
	else:
		pass
		#Allows the user to decide to keep spinning the wheel or exit
		user_input = input("Spin the wheel?(y/n): ")
		if user_input == "y":
			#Allows betting a certain number of tokens
			placed_bet = input("How much would you like to bet? (Minimum buy is 1 token): ")
			placed_bet = float(placed_bet)
			if placed_bet > balance:
				print("You don't currently have that many tokens")
			elif placed_bet < 1:
				print("That bet is too low. Minimum bet is 1 token")
			else:
					#Spins the wheel
					balance -= placed_bet
					reward = 0
					reel_1, reel_2, reel_3 = [ran.choice(weighted_numbers) for i in range(3)]
					print("spinning...")
					t.sleep(1)
					print("You got", reel_1, reel_2, reel_3)
					if reel_1 == reel_2 == reel_3:
						win(3, reel_1)
					elif reel_1 == reel_2 or reel_1 == reel_2 or reel_2 == reel_3:
						if reel_2 == reel_3:
							win(2, reel_2)
						else:
							win(2, reel_1)
					else:
						print("Aww man! Looks like none of your numbers matched!")
					print("Your balance is", balance)
		elif user_input == "n":
			print("Hope you had fun!")
			break
		else:
			print("invalid response, please type y or n")