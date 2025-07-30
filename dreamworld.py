'''
    Name: Dreamworld eleigability
    Version: 1.0.0
    Description: Program for checking if ur eligible for dreamworld rides

'''
#---------------main------------------
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
rides = [] # Empty list that will contain eligible rides

if height > 150:
    for ride in "Stratosfear,Family Karts,Scorpion Karts".split(','):
        rides.append(ride)
if height >120:
    for ride in "Fearfall,Invader,Corkscrew Roller Coster,Bumber boatrs".split(','):
        rides.append(ride)
if height > 90 and age >= 5:
    rides.append("Los Banditos")
if height>90 and age == 8:
    rides.append("Robot Riot")
if height > 80:
    for ride in "Log Flume,Gold Rush,Family Karts(passenger),Dogems(passeenger)".split(','):
        rides.append(ride)
elif age >= 3 and age <= 8:
    rides.append("Fortress of Fun")

print("You are eligible for:",end=" ")
for ride in rides:
    print(ride,end=", ")
print()
    