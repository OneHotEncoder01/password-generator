#!/usr/bin/env python
import words_password
import chars_password

def main():
	print("(1)random characters")
	print("(2)random words and numbers")

	a = int(input("enter 1 or 2 = "))

	if (a == 1):
		chars_password.main()
	elif (a == 2):
		words_password.main()
	else:
		print('you can only enter 1 or 2')
		input('press Enter')
		main()

if __name__ == '__main__':
	main()