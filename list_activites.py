'''
    name: List Activites
    description: Activites using lists.

'''
#--------------libraries------------------
import random

student_list = ['Jenna','Bob','Tim','Greg','Jimmy']

counter = 0
while counter < len(student_list):
    print(counter+1,student_list[counter])
    counter += 1