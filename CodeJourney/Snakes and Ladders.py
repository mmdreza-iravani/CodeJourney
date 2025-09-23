
#Snakes and ladders with computer

import random

def main():

	TARGET = 100

	USER_POINT = 0
	PC_POINT = 0

	explanation()
	
	USER_NAME = input("Enter your name: ").capitalize()
	PC_NAME = 'Computer'

	while True:

		#user
		input("\nIt's your turn. Enter something to roll: ")
		user_roll = rolling()
		USER_POINT = move(USER_POINT, user_roll, USER_NAME, TARGET)

		#pc
		pc_roll = rolling()
		PC_POINT = move(PC_POINT, pc_roll, PC_NAME, TARGET)
		

		print('-------------')


def explanation():
	# Explain the Game to user
	print()
	print(" Welcome to SNAKES AND LADDERS Game! ".center(56, '=') + '\n')
	while True:
		order = input("Do you want to read the explanation of the game? (y/n): ").lower()

		if order in ['y', 'yes', 'yepp', 'of course', 'sure']:
			print("""
	In this game you play with computer,
	You roll to reach the 100 point.
	But it is not that easy, there some snakes in the way 
	that if you touch them, they will pull you back in previous positions.
	Also there are some ladders in the way that you can use them and go higher.
				""")
			break

		elif order in ['n', 'no', 'nope', 'not really', 'not intereted']:
			print("Okay, no explanation :)")
			break

		else:
			print("Invalid, try again.")


def rolling():
	# Roll the dice randomly for each player
	roll = random.randint(1, 6)
	return roll


def move(point, roll, name, TARGET):
	# Change player's position in every roll
	
	if point == 0:

		if roll == 6:
			point = 1
			print(f"{name} rolled 6 and entered in the game. Your current point is {point}.")

		else:
			print(f"{name} rolled {roll}. For entering in the game, must roll 6.")
			point = 0


	elif point != 0:
		new_point = point + roll
		print(f"{name} rolled {roll}.")

		new_point = snakes(new_point, name)
		new_point = ladders(new_point, name)
		
		result = win_check(new_point, name, TARGET)
		if result == 'win':
			if name != 'Computer':
				print("Congratulations!")
			print(f"{name} reached 100 point and won the game.")
			play_again()
		elif result == 'pass':
			print(f"{name} can not go higher than 100! So the roll wasted.")
		else:
			point = new_point

		print(f"{name}'s current point is {point}")
			

		while True:
			if roll == 6:
				print(f"As {name} rolled 6, has another chance to roll: ")
				new_point, roll = prize6(roll, new_point, name)
				print(f"{name} rolled {roll}.")

				new_point = snakes(new_point, name)
				new_point = ladders(new_point, name)
				
				result = win_check(new_point, name, TARGET)
				if result == 'win':
					if name != 'Computer':
						print("Congratulations!")
					print(f"{name} reached 100 point and won the game.")
					play_again()
				elif result == 'pass':
					print(f"{name} can not go higher than 100! So the roll wasted.")
				else:
					point = new_point

				print(f"{name}'s current point is {point}")	
				continue
			else:
				break

	return point


def prize6(roll, point, name):
	# If the user rolled 6 in the game except the start of the game, have another chance to roll
	if name == 'Computer':	#For pc
		prize = rolling()
		point = point + prize

	else:	#For user
		input("Enter something to roll your prize: ")
		prize = rolling()
		point = point + prize	



	return point, prize


def snakes(point, name):
	# Whenever the player stands at the below points, snakes will pull the player back
	if point in [27, 40, 43, 54, 66, 89, 95, 99]:

		if point == 27:
			print("oh, there was a snake on position 27!")
			point = 5

		elif point == 40:
			print("oh, there was a snake on position 40!")
			point = 3

		elif point == 43:
			print("oh, there was a snake on position 43!")
			point = 18

		elif point == 54:
			print("oh, there was a snake on position 54!")
			point = 31

		elif point == 66:
			print("oh, there was a snake on position 66!")
			point = 45

		elif point == 89:
			print("oh, there was a snake on position 89!")
			point = 53

		elif point == 95:
			print("oh, there was a snake on position 95!")
			point = 77

		elif point == 99:
			print("oh, there was a snake on position 99!")
			point = 41

		return point

	else:
		return point


def ladders(point, name):
	# Whenever the player stands at the below points, ladders will pull the player up
	if point in [4, 13, 42, 50, 62, 74]:

		if point == 4:
			print("Wow, there was a ladder on position 4!")
			point = 25

		elif point == 13:
			print("Wow, there was a ladder on position 13!")
			point = 46

		elif point == 42:
			print("Wow, there was a ladder on position 42!")
			point = 63

		elif point == 50:
			print("Wow, there was a ladder on position 50!")
			point = 69

		elif point == 62:
			print("Wow, there was a ladder on position 62!")
			point = 81

		elif point == 74:
			print("Wow, there was a ladder on position 74!")
			point = 92

		return point

	else:
		return point


def win_check(point, name, TARGET):
	# Check if the player win the game
	# and also don't let the player go higher than 100

	if point == TARGET:
		return 'win'

	elif point > TARGET:
		return 'pass'

	else:
		return 'continue'


def play_again():
	# Ask the users if wanna play again or not
	while True:
		ask_continue = input("Do you want to play again? (y/n): ").lower()
		if ask_continue in ['y', 'yes']:
			main()
		elif ask_continue in ['n', 'no']:
			print("Okay, good bye.")
			quit()
		else:
			print("Invalid, try again.")


# ---- main program ----

main()



