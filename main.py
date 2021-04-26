"""
SPS (Python)

Created on : April 25, 2021

Author : Rishav Das
"""

# Importing the required functions and modules
try:
	from sys import platform
	from os import system
	from random import randint
except Exception as e:
	# If there are any errors during the importing of modules, then we raise an error

	print('[ Error : Failed to import some of the modules, please check them ]')

# Defining the ANSII color variables for colored output
if 'linux' in platform:
	# Defining the color variables only if the platform type is linux

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	green_rev = '\033[07;92m'
	defcol = '\033[00m'
else:
	# If the platform type is not linux, then we make the color variables blank

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	green_rev = ''
	defcol = ''

# Defining the clear screen command as per the operating system
if 'linux' in platform:
	# Using the 'clear' command if the operating system type is of linux

	clear = lambda : system('clear')
else:
	# Using the 'cls' command if the operating system type is of not linux (it is windows)

	clear = lambda : system('cls')

# The main script starts here

def main():
	""" DRIVER CODE """

	score = 0
	while True:
		# Playing the game in loop such that the game lasts for long until the user chooses to stop the game

		clear()
		print()
		print('[ ' + blue + 'Current score : ' + yellow + str(score) + defcol + ' ]')
		print('{yellow}Choose any {green}[ {blue}Stone, Paper, Scissors {green}]'.format(yellow = yellow, green = green, blue = blue) + defcol)
		choice = input(blue + 'Enter your choice : ' + yellow).lower()
		print(defcol, end = '')

		# Getting the computer automated selection
		computerChoice = ['stone', 'paper', 'scissors'][randint(0, 2)]

		# Checking the user input and estimating the current play's score
		if choice == 'stone' or choice == '1' or choice == 'a':
			# If the user choosed stone as the choice, then we proceed further for evaluation

			if computerChoice == 'stone':
				# If the computer chooses the stone, then we can say its draw

				print('[ ' + yellow + 'Draw' + defcol + ' : The computer also choosed stone ]')
			elif computerChoice == 'paper':
				# If the computer chooses the paper, then we can say its loss

				score -= 10
				print('[' + red + 'Lost' + defcol + ' : The computer choosed paper ]')
			elif computerChoice == 'scissors':
				# If the computer chooses the scissors, then we can say its win

				score += 5
				print('[' + green + 'Win' + defcol + ' : The computer choosed scissors ]')
		elif choice == 'paper' or choice == '2' or choice == 'b':
			# If the user chooses the paper as its choice, then we proceed further for evaluation

			if computerChoice == 'stone':
				# If the computer chooses the stone, then we can say its won

				score += 5
				print('[' + green + 'Won' + defcol + ' : The computer choosed stone ]')
			elif computerChoice == 'paper':
				# If the computer chooses the paper, then we can say its draw

				print('[ ' + yellow + 'Draw' + defcol + ' : The computer also choosed paper ]')
			elif computerChoice == 'scissors':
				# If the computer chooses the scissors, then we can say its loss

				score -= 10
				print('[' + red + 'Loss' + defcol + ' : The computer choosed scissors ]')
		elif choice == 'scissors' or choice == '3' or choice == 'c':
			# If the user chooses the scissors as its choice, then we proceed further for evaluation

			if computerChoice == 'stone':
				# If the computer chooses the stone, then we can say its loss

				score -= 10
				print('[' + red + 'Loss' + defcol + ' : The computer choosed stone ]')
			elif computerChoice == 'paper':
				# If the computer chooses the paper, then we can say its won

				score += 5
				print('[ ' + green + 'Won' + defcol + ' : The computer choosed paper ]')
			elif computerChoice == 'scissors':
				# If the computer chooses the scissors, then we can say its draw

				print('[' + yellow + 'Draw' + defcol + ' : The computer choosed also scissors ]')
		else:
			# If the user chooses any other option, then we raise the error that there is no such options available

			print(red_rev + '[ Error : No such options allowed. Choose only from stone, paper, scissors ]' + defcol)
				
		# Printing the score on the computer screen for the current round
		print('[ ' + blue + 'Score : ' + defcol + str(score) + ' ]')

		# Asking the user wheter he/she wants to go for another round or just end the game here
		choice = input(blue + '\nWant to stop here (y to exit, enter key to continue) : ' + yellow).lower()
		if choice == 'y' or choice == 'yes':
			# If the user chooses to end the game here, then we proceed to displaying the final score and end the game here

			print()
			print(green + 'FINAL SCORE : ' + yellow + str(score) + defcol)
			print(blue + 'Thanks for playing the game..!' + defcol)
			break
		else:
			# If the user enters any input other than 'y' or 'yes', then we continue for the next iteration

			continue

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combination, then we quit the script

		quit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message to the user on the console screen

		print(red_rev + '[ Error : {} ]'.format(e) + defcol)
