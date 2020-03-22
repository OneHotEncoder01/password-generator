#!/usr/bin/env python
import string
import random
def main():
	length_char = int(input("enter length of letters = "))
	length_num = int(input("enter length numbers = "))
	list_pass = string.printable[:62]
	password = ''
	a = len(list_pass)
	for i in range(length_char):
		password+=list_pass[random.randint(1,a-1)]
	for _ in range(length_num):
		password+=str(random.randint(0,9))

	print(password)

	input('')

if __name__ == '__main__':
	main()