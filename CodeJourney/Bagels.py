
# BAGELS Game

import random


def main():
	
	DIGITS_NUM = 3

	CHANCES = 10


	explanation(DIGITS_NUM, CHANCES)

	choose_number()

	take_guess(CHANCES, DIGITS_NUM)



def explanation(DIGITS_NUM, CHANCES):
	# Explain the game to user
	print()
	print(" BAGELS Game! ".center(27, '=') + '\n')
	print(f"I am thinking of a {DIGITS_NUM}-digit number. Try to guess what it is. ")
	print("""
Here are some clues:
When I say:  /   That means:
   Fermi    =>    One digit is correct and in the right position.
   Pico     =>    One digit is correct but in the wrong position.
   Bagels   =>    No digit is correct.
   \n """)



def choose_number():
	# Let the computer choose a random {digits_num} digits numebr
	numbers = list('1234567890')
	random.shuffle(numbers)

	secret_number = numbers[:3]
	print("I have thought up a number.")
	return secret_number



def take_guess(CHANCES, DIGITS_NUM):
	# Take guesses from the user
	print(f"You have {CHANCES} guesses to get it.")
	number_in_list = choose_number()
	secret_number = ''.join(number_in_list)

	tries = 0

	while True:

		is_lose(CHANCES)

		tries += 1

		while True:
			guess = input(f"Guess {tries}#: \n> ")

			if len(guess) != DIGITS_NUM:
				print(f"Enter only {DIGITS_NUM} digits number!")
			else:
				break

		is_win(guess, secret_number)

		clues, CHANCES = game_hint(guess, secret_number, CHANCES)

		print(' '.join(clues))



def game_hint(guess, secret_number, CHANCES):
	# Help the user to find the secret number with giving some hints to user
	clues = []
	CHANCES -= 1
	for number in range(len(secret_number)):
		if guess[number] == secret_number[number]:
			clues.append('Fermi')

		elif guess[number] in secret_number:
			clues.append('Pico')

		else:
			clues.append('Bagels')

	return clues, CHANCES



def is_win(guess, secret_number):
	# Check the guess if it is completely correct
	if guess == secret_number:
		print("Congratulations! You guessed the number.")
		play_again()



def is_lose(CHANCES):
	# If the player lose all chances, will lose the game
	if CHANCES == 0:
		print("You ran out of chances and lost the game.")
		play_again()



def play_again():
	# Ask the user if want to play again or not
	while True:
		ask_continue = input("DO you wanna play again? ").lower()

		if 'yes' in ask_continue.split() or ask_continue in ['y', 'yepp', 'sure', 'of course']:
			main()


		elif 'no' in ask_continue.split() or ask_continue in ['n', 'nope']:
			print("Okay, good bye!")
			quit()

		else:
			print("Invalid, try again.")

# --- main program ---

main()



