'''
    Name: Driver Licence
    Description: Python file containing a basic drivers licence 
    Author: MEEEEEE
    Date: 29/07/2025
'''
#---------------libraries----------------------
#No libraries needed!!!

#--------------functions-----------------------
def is_over_16(yrs,mnths): 
    if yrs + mnths/12 > 16.5: 
        return True
    else:
        return False
    
def held_for_6_months(dur):
    if dur >= 6:
        return True
    else: 
        return False
    
#--------------main routine--------------------
age = input("Enter your in years and months (years,months): ")
years,months = age.split(',')

months_with_learners = int(input("How many months have you had your learners licence for? "))

if is_over_16(int(years),int(months)) and held_for_6_months(months_with_learners):
    print("You can get your ristricted.")
else:
    print("You can't get your restricted")
    
