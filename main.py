"""
SPS (Python)

Created on : April 25, 2021

Author : Rishav Das
"""

# Importing the required functions and modules
try:
	from sys import platform
	from os import system
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

	return 0

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combination, then we quit the script

		quit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message to the user on the console screen

		print(red_rev + '[ Error : {} ]'.format(e) + defcol)
