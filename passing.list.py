'''
    author: MEE
    date: 11/08/2025
    version: 1.0.0
    description: A bunch of things you can do with lists, names, and numbers.

'''
#----------------functions---------------------
def force_name():
    name = input("Enter your name: ")
    while not(len(name) > 1 and len(name) < 20 and name.isalpha()):
        print("ERROR: Your name is weird")
        name = input("Enter a normal name: ")
    return name

def force_age():
    age = 0
    while True: 
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("ERROR: Age needs to be a number.")
            continue
        if age > 1 and age < 150:
            return age
        print("ERROR: Age is an invalid number.")

def introduce(name,age):
    print(f"Your name is {name}.\nYou are {age} years old.")

#---------------main routine-------------------------
name = force_name()
age = force_age()
introduce(name,age)
print("BYE")

