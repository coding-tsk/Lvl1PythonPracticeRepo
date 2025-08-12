'''
    author: MEEEE
    date: 04/08/2025
    version: 1.0.0
    description: A simple number guessing game
'''
#-----------------libraries--------------------
from random import randint
#--------------------functions--------------------
def force_num():
    # Hardcoding True in condition is a bad practice but is good enough for lvl 1
    while True: 
        try:
            num = int(input("Guess the number: "))
            if num >= 1 and num <= 10:
                return num
            print("The number needs to be between 1 and 10.")
        except ValueError:
            print("You need to enter a number.")

def force_name():
    name = input("What's your name? ")
    while (not name.isalpha()) or len(name) < 2 or len(name) > 20: 
        print("Your name is weird.")
        name = input("Enter a normal name: ")
    return name
#---------------main routine----------------------
name = force_name()
num = randint(1,10)
print("I've chosen a number from 1 to 10.")

gusses = 0
while True:
    guess = force_num()
    gusses += 1
    if guess > num:
        print("Your guess is too large. Try again.")
    elif guess < num:
        print("Your guess is too small. Try again.")
    else:
        break


print(f"You guessed the number!!! It took you {gusses} gusses")
print("Bye,",name.capitalize())
    
