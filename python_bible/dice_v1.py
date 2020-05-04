#!/usr/bin/python3
#Program to simulate a die roll with a pearson against computer
from random import randint
import time
def rollDieFunc():
    dieValue = randint(1,6)
    return dieValue;

#Variaveis
play = 'x'
playAgain = 'y'
playerName = ''
playerValue = 0
computerValue = 0
while (play != '' and play != 'q'):
    play = input("Press (Enter) to play or (q) to quit:")
    print(play)

if play == "":
    playerName = input("Enter your Name: ")
    print(playerName)
    while (playAgain == 'y'):
        playerValue = rollDieFunc()
        print(playerName," value: ",playerValue)
        print("Computer's turn...")
        computerValue = rollDieFunc()
        time.sleep(3)
        print("Computer's value: ",computerValue)
        if (playerValue > computerValue):
            print(playerName," win!")
        elif (playerValue < computerValue):
            print("Computer win!")
        else:
            print("Tie in the game!")
        playAgain = input("Play again (y/n)?")
        if (playAgain == 'n'):
            print("Bye!")
else:
    print("Bye!")