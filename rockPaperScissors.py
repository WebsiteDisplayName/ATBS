import random
import sys

print('ROCK, PAPER, SCISSORS')

Wins = 0
Losses = 0
Ties = 0


while True:
    print(f"{Wins} Wins, {Losses} Losses, {Ties} Ties")
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        response = input()
        if response == "q":
            sys.exit()
        elif response == "r" or response == "p" or response == "s":
            break
        else:
            print("Please enter: r, p, s, or q") 



    
    if response == 'r':
        print('ROCK versus...')
    elif response == 'p':
        print('PAPER versus...')
    elif response == 's':
        print('SCISSORS versus...')

    versusOpponent = random.randint(0,2)
    if versusOpponent == 0:
        versusOpponent = 'r'
        print("ROCK")        
    elif versusOpponent == 1:
        versusOpponent = 'p'
        print("PAPER")
    elif versusOpponent == 2:
        versusOpponent = 's'
        print("SCISSORS")

    if response == versusOpponent:
        print("It is a tie!\n")
        Ties += 1
    elif (response == 'r' and versusOpponent == 's') or (response == 'p' and versusOpponent == 'r') or (response == 's' and versusOpponent == 'p'):
        print('You win!\n')
        Wins += 1
    elif (response == 's' and versusOpponent == 'r') or (response == 'r' and versusOpponent == 'p') or (response == 'p' and versusOpponent == 's'):
        print('You lose!\n')
        Losses += 1
