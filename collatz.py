import sys


def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

while True:
    try:
        print("Please enter a number: ", end='')
        response = int(input())

        while True:
            response = collatz(response)
            if response == 1:
                sys.exit()

    except ValueError:
        print('Please enter an integer.\n')
