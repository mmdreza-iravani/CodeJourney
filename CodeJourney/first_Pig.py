#PIG game

import random

def main():
	FINAL_POINT = 50

	USER1_POINT = 0
	USER2_POINT = 0

	USER1_NAME, USER2_NAME = greet()
	while True:

		#User
		USER1_POINT = decide_to_roll(USER1_NAME, USER1_POINT, FINAL_POINT)
		print(f"{USER1_NAME}'s point: {USER1_POINT}")
		if USER1_POINT >= FINAL_POINT:
			break

		#PC
		USER2_POINT = decide_to_roll(USER2_NAME, USER2_POINT, FINAL_POINT)
		print(f"{USER2_NAME}'s point: {USER2_POINT}")
		if USER2_POINT >= FINAL_POINT:
			break

	play_again()


def greet():
	# Greet with the user and explain the game
	print()
	print(" Welcome to PIG Game! ".center(56, '=') + '\n')

	USER1_NAME = input("Enter the name of the player1: ").capitalize()
	USER2_NAME = input("Enter the name of the player2: ").capitalize()

	explaining = game_explainaton()
	if explaining == 'yes':
		print("""
	Rules of the Game:

 		-The goal is to reach 50 points.
	 	-On each turn, a player rolls a dice as many times as they like.
	 	-Each roll adds to their turn total.
	 	-BUT if the player rolls a 1, they lose all points from that turn! Their overall score stays the same, but their turn ends immediately.
	 	-A player can choose to "hold". This means they add the turn total to their overall score, and their turn ends safely.
	 	-Players take turns until one of them reaches the target score.
			""")
	print("Let's start rolling!\n")

	return USER1_NAME, USER2_NAME


def game_explainaton():
	# Explain the game for the user
	while True:	
		order = input("Do you want me to explain the rules of the game? (y/n): ").lower().strip()

		if order in ['y', 'yes', 'yepp', 'yeah', 'of course', 'sure', 'yes of course']:
			return 'yes'
			break
		elif order in ['n', 'no', 'nope', "i'm not interested", 'not really', 'no thanks']:
			print("Okay, no explaination :)")
			break
		else:
			print("Invalid, please try again.")


def rolling():
	# Roll the dice
	roll = random.randint(1, 6)

	return roll


def decide_to_roll(name, point, FINAL_POINT):
	# The decition of each player to how many times wanna roll

	input(f"\nIt's {name}'s turn, enter anything to roll: ")
	roll = rolling()

	print(f"{name} rolled {roll}")

	if roll == 1:
		point = bomb(point)
		return point

	point += roll
	print(f"{name}'s current point is {point}.")

	if point >= FINAL_POINT:
		is_win(name)
		return point

	while True:
		order = input(f"Enter anything to roll again or (stop to quit): ").lower()
		if order == 'stop':
			break
		else:
			roll = rolling()
			print(f"{name} rolled {roll}")

			if roll == 1:
				point = bomb(point)
				return point

			point += roll
			print(f"{name}'s current point is {point}.")

			if point >= FINAL_POINT:
				is_win(name)
				return point

	return point


def bomb(point):
	# If the player roll 1, will lose all his points
	print("Wow, you lost all of your points!")
	point = 0

	return point


def is_win(name):
	# Check if the player reach the point 50
	print(f"Congratulaions! {name} won the game!")


def play_again():
	# Ask the users if they want to play again
	while True:
		ask_continue = input("Do you want to play again? (y/n): ")
		if ask_continue in ['y', 'yes', 'yepp', 'yeah', 'of course', 'sure', 'yes of course']:
			main()
			break
		elif ask_continue in ['n', 'no', 'nope', "i'm not interested", 'not really', 'no thanks']:
			print("Okay, good bye.")
			quit()
		else:
			print("Invalid, please try again.")


# ---- Main Program ----

main()

