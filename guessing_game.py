'''
    author: MEEEE
    date: 04/08/2025
    version: 1.0.0
    description: A simple number guessing game
'''
#-----------------libraries--------------------
from random import randint
#--------------------functions--------------------

#---------------main routine----------------------
name = input("What's your name? ")
num = randint(1,10)
print("I've chosen a number from 1 to 10.")

gusses = 0
while True:
    guess = int(input("Guess the number: "))
    gusses += 1
    if guess > num:
        print("Your guess is too large. Try again.")
    elif guess < num:
        print("Your guess is too small. Try again.")
    else:
        break


print(f"You guessed the number!!! It took you {gusses} gusses")
    
