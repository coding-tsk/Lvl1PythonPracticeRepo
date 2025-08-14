'''
    author: name
    date: 15/08/2025
    version: 1.0.0
    description: Python script to go on an adventure :)
'''
#---------------------libraries---------------------------
import random #lib for random numbers
#---------------------functions---------------------------

#---------------------main routine------------------------
if __name__ == "__main__":
    hp = 100 # player hitpoints
    dff = 15 #player defence
    en_hp = 100 #enemy hitpoints
    en_dff = 15 #enemy defence

    #battle loop
    while(hp > 0 and en_hp > 0): #while both player and enemy are alive
        attack = input('''
    Enter your move:
        [s]word
        [a]xe
        [h]eal''')[0].lower() #first letter of lowercase input
        
        #Checking what user entered
        if(attack == 's'): #sword attack
            pass
        if(attack == 'a'): #axe attack
            pass
        if(attack == 'h'): #heal
            pass
        else: #not valid move
            print("Not a valid move. Try again.")
            continue # back to start of loop