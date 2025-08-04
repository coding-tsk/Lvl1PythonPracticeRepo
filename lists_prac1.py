'''
    author: Myself
    date: 04/08/2025
    version: 1.0.0
    description: List functions to use
'''

#--------------libraries---------------------
from random import shuffle

#-----------------functions---------------------


#---------------main program---------------------
sports = ["Football","Rugby","Hockey","Basketball","Cricket","Volleyball"]
sports.append("Tennis")

print(sports)
shuffle(sports)
print(sports)