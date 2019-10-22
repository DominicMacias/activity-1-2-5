#!/usr/bin/python3
#Dominic Macias and Gentry Cross
#10/12/19

#Imports
import random as ran
import time as t
import pickle as p

#Main functions defined
def win(number_of_matches, number):
	global balance
	global placed_bet
	print("Congrats! You got", number_of_matches, "of the same number!")
	reward = (numbers[number][1] * number_of_matches) * placed_bet
	print("You won", reward, "tokens!")
	balance += reward

def wheel_spin():
	global balance
	balance -= placed_bet
	reward = 0
	for i in range(4):
		reel_1, reel_2, reel_3 = [ran.choice(weighted_numbers) for i in range(3)]
		print("Spinning...")
		t.sleep(.5)
		#Wheel Overlay
		print("""
				      .-------.
				      |Jackpot|
			  ____________|_______|____________
			 |  __    __    ___  _____    __   |  
			 | / _\  / /   /___\/__   \  / _\  | 
			 | \ \  / /   //  //  / /\ \ \ \   |  
			 | _\ \/ /___/ \_//  / /  \/ _\ \[]| __
			 | \__/\____/\___/   \/      \__/[]|(__)
			 |===_______===_______===_______===| ||
			 ||*|       |*|       |*|       |*|| ||""")
		print("                         ||*|  ",reel_1,"  |*|  ",reel_2,"  |*|  ",reel_3,"  |*|| ||")
		print("""                         ||*|_______|*|_______|*|_______|*||_//
			 |===_______===_______===_______===|_/
			 |lc=___________________________===|
			 |  /___________________________\  |
			 |   |                         |   |
			_|    \_______________________/    |_
		       (_____________________________________)
		       """)
	if reel_1 == reel_2 == reel_3:
		win(3, reel_1)
	elif reel_1 == reel_2 or reel_1 == reel_3 or reel_2 == reel_3:
		if reel_2 == reel_3:
			win(2, reel_2)
		else:
			win(2, reel_1)
	else:
		print("Aww man! Looks like none of your numbers matched!")	

#Extra Commands
def save_data():
	print("Saving...")
	filename = 'token'
	outfile = open(filename, 'wb')
	p.dump(balance,outfile)
	outfile.close()
	print("Data saved")

def list_chance():
	print(" 1->  25.9%\n 2->  18.2%\n 3->  15.6%\n 4->  13.0%\n 5->  10.4%\n 6->  7.8%\n 7->  5.2%\n 8->  2.6%\n 9->  1.3%\n 10-> 0.0026%")
	print(" *These are the chances for a single reel")

def list_rewards():
	print(" Pair of 1's  -> 2\n All 1's      -> 3\n Pair of 2's  -> 4\n All 2's      -> 6\n Pair of 3's  -> 6\n All 3's      -> 9\n Pair of 4's  -> 8\n All 4's      -> 12")
	print(" Pair of 5's  -> 10\n All 5's      -> 15\n Pair of 6's  -> 12\n All 6's      -> 18\n Pair of 7's  -> 20\n All 7's      -> 30")
	print(" Pair of 8's  -> 40\n All 8's      -> 60\n Pair of 9's  -> 200\n All 9's      -> 300\n Pair of 10's -> 20,000\n All 10's     -> 30,0000")
	print(" *These are multiplied by the amount of tokens placed on the bet")
	
#Signifies each items chance and reward
numbers = {1: [10000, 1], 2: [7000, 2], 3: [6000, 3], 4: [5000, 4], 5: [4000, 5], 6: [3000, 6], 7: [2000, 10], 8: [1000, 20], 9: [500, 100], 10: [1, 10000]}
weighted_numbers = [number for number in numbers for i in range (numbers[number][0])]

print("                          Welcome to the Slot Machine!")
print("                   type in 'y' to spin the wheel, or 'n' to exit.")
print("                         Enter 'help' for more commands")
balance = 10

print("Your remaining balance is", balance)

#Main gambling function
while True:
	#Prevents betting with no tokens on the slot machine
	if balance <= 0:
		print("Sorry, but you dont have any more money to gamble with. Hopefully you can come again sometime!")
		break
	else:
		pass
		#Allows the user to decide to spin the wheel, exit, or another command
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
				wheel_spin()
			print("Your balance is", balance)


		elif user_input == "help":
			print("""'y' to spin the wheel
'n' to exit the program
'chance' to see the list of chances for each number
'rewards' to see the list of rewards
'save' to save your progess
'load' to load your save""")
		elif user_input == "chance":
			list_chance()
		elif user_input == "rewards":
			list_rewards()
		elif user_input == "n":
			print("Hope you had fun!")
			break
		elif user_input == "save":
			save_data()
		elif user_input == "load":
			print("Loading...")
			filename = 'token'
			infile = open(filename, 'rb')
			new_balance = p.load(infile)
			infile.close()
			balance = new_balance
			print("Data Loaded")
			print("Your balance is now", balance)			
		else:
			print("invalid response, please type y or n")