
# Rock, Paper and Scissors Game

import random
import sys

choices = ['r', 'p', 's']

def main():
	print(" Welcome to ROCK-PAPER-SCISSORS Game! ".center(56, '=') + '\n')
	print("In this program, you play againts computer.")
	print("Let's go.")

	while True:
		user_choice = user(choices)
		display_user_choice = translate(user_choice)
		print(f"You chose {display_user_choice}.")

		pc_choice = pc(choices)
		display_pc_choice = translate(pc_choice)
		print(f"Computer chose {display_pc_choice}.")

		comparing(user_choice, pc_choice)

		if ask_continue():
			continue
		else:
			print("Good bye.")
			sys.exit()

def pc(choices):
	# PC choose randomly
	pc_choice = random.choice(choices)

	return pc_choice

def user(choices):
	# Get user's choice
	while True:
		user_choice = input("Choose one (just the first letter => 'r'ock, 'p'aper, 's'cissors): ")
		if user_choice not in choices:
			print("Please enter just these commands: r, p, s\n")
			continue
		else:
			break
	return user_choice

def comparing(user_choice, pc_choice):
	# Determine the win or tie
	if user_choice == pc_choice:
		print("It's a tie.")

	elif (
		(user_choice == 'r' and pc_choice == 's') or
		(user_choice == 's' and pc_choice == 'p') or 
		(user_choice == 'p' and pc_choice == 'r')
		):
		print("You won.")

	else:
		print("You lost.")

	print()

def translate(choice):
	# Translate the small letter into its word like r => rock
	if choice == 'r':
		choice = 'rock'
	elif choice == 'p':
		choice = 'paper'
	else:
		choice = 'scissors'

	return choice

def ask_continue():
	# Ask the user if wanna play again
	while True:	
		order = input("Do you wanna play again? (y/n): ").lower()
		if order == 'y':
			return True
			break
		elif order == 'n':
			return False
			break
		else:
			print("Please enter only y or n.")


main()

