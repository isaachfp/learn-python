#!/usr/bin/python3
#Program to simulate a die roll with a pearson against computer
from random import randint
def rollDieFunc():
    dieValue = randint(1,6)
    return dieValue;

#Variaveis
play = 'x'
playerValue = 0
computerValue = 0
print(play)
while (play != '' and play != 'q'):
    play = input("Press (Enter) to play or (q) to quit:")
    print(play)

if play == "":
    print("Enter key pressed")
    print(play)
    x = rollDieFunc()
    print(x)
else:
    print("You choose quit")