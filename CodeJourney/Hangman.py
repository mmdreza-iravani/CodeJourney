
# HANGMAN Game

import random

words = ['python', 'forest', 'dragon', 'silver', 'circle', 'castle', 'hunter', 'driver', 'office', 'school', 'lawyer', 'doctor', 'dancer', 'singer', 'basket', 'summer']

letters = []


def main():

	TRIES = 7

	explanation()

	secret_word = choose_word(words)

	take_guess(secret_word, TRIES, letters)



def take_guess(secret_word, TRIES, letters):
	# Take guess from the user => letter by letter
	
	hidden_word = hide_word(secret_word)

	display_prettier = ' '.join(hidden_word)

	print(f"Secret word: {display_prettier}")
	
	while True:

		guess = input("\nTry to guess a letter: ").lower()

		if len(guess) > 1:
			print("Enter only a letter each time!")
			continue

		elif guess == '':
			print("You typed nothing.")
			continue

		elif guess not in secret_word:
			TRIES -= 1
			if TRIES == 0:
				print("\nYou lost!\n")
				play_again()
			print(f"You guessed wrong! You have only {TRIES} tries left!")

		elif guess in letters:
			print(f"You have already guessed {guess}!")

		#Update
		for letter in range(len(secret_word)):
			if guess == secret_word[letter]:
				hidden_word[letter] = guess
				letters.append(guess)
		print(f"Secret word: {' '.join(hidden_word)}")

		check_for_win(hidden_word, letters)



def check_for_win(hidden_word, letters):
	# Check if the user guessed all the letters in the secret word

	if '_' not in hidden_word:
		print("Congratulations! You guessed it.\n")
		letters.clear()
		play_again()



def explanation():
	# Greet and explain the game for the user
	print()
	print(" Welcome to HANGMAN Game! ".center(56, '=') + '\n')

	while True:
		ask_explanation = input("Do you want to read the game explanation? (y/n): ").lower()

		if ask_explanation in ['y', 'yes', 'sure', 'of course', 'yes of course']:
			print("""\nHere is the hangman game explanation:
In this game there are some words that the computer chooses one randomly,
then you should guess this secret word letter by letter to complete all the letters.
You have only 7 tries and if you lose all your tries, the hangman will be dead!\n""")
			break

		elif ask_explanation in ['n', 'no', 'nope', 'no thanks']:
			print("Okay, no explanation :)")
			break

		else:
			print("Invalid, try again.")



def choose_word(words):
	# Let the computer choose a word from the list randomly
	input("Enter something to let the computer choose a word: ")
	word = random.choice(words)
	print("Computer chose a word randomly.")
	return word



def hide_word(secret_word):
	# Hide the word from the user like this _ _ _ _
	
	hidden_word = len(secret_word) * ['_']

	return hidden_word



def play_again():
	#Ask the user if want to play again or not
	while True:
		ask_continue = input("Do you wanna play again? (y/n): ").lower()

		if ask_continue in ['y', 'yes', 'sure', 'of course', 'yes of course']:
			main()

		elif ask_continue in ['n', 'no', 'nope', 'no thanks']:
			print("Okay, good bye!")
			quit()

		else:
			print("Invalid, try again.")


# --- main program ---

main()

