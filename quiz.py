'''
    author: mee
    date: 12/08/2025
    version: 1.0.0
    description: Simple quiz

'''
#--------------functions---------------------
def force_str(question):
    ans = input(question)
    while not ans.isalpha():
        print("Answer needs to only have letters")
        ans = input(question)
    return ans

def force_int(question):
    ans = input(question)
    while not ans.isnumeric():
        print("Answer needs to be a number.")
        ans = input(question)
    return ans

#-------------main routine--------------------
questions = [
    "How many letters are in the english alphabet, including upper and lower case letters? ",
    "What is the longest river in New Zealand? ",
    "What is the longest river in the world?",
    "What is the largest planet in the solar system? "
    "What school do you go to? "
    ]

answers = [
    "26",
    "Waikato River",
    "Nile",
    "Jupiter",
    "Otago Boys High School"
    ]

q_type = [force_int,force_str,force_str,force_str,force_str]

for q in range(5):
    ans = q_type[q](questions[q])
    if ans == answers[q]:
        print("The answer is correct.")
