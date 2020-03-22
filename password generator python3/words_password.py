import random

def main():
    password = ''
    lines_list = open('words.txt').read().splitlines()
    num_words = int(input('Enter the number of words = '))
    for i in range(num_words):
        password += lines_list[random.randint(0, len(lines_list))]

    num_number = int(input('Enter the number of numbers = '))
    for i in range(num_number):
        password += str(random.randint(0, 9))

    print (
     'the password is --> ', password)

    k = input(' ')

if __name__ == '__main__':
    main()