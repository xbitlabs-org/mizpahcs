# class 6, 7

import random

def main():
	number = random.randint(1, 10)
	player_name = input('Enter your name : ')
	print('You have 5 attempts to guess the number')
	no_guesses = 0

	while no_guesses < 5:
		guess = int(input('Enter a number to guess: '))
		no_guesses +=1

		if guess < number:
			print('Your guess is too low')
		elif guess > number:
			print('Your guess is too high')

		elif guess == number:
			print('You guessed the number in : ', no_guesses, ' tries')
			exit()
			
if __name__ == '__main__':
	main()

