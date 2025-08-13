'''
    author: mee
    date: 12/08/2025
    version: 1.0.0
    description: Simple quiz

'''
#--------------functions---------------------
#Make sure the user types a one word alphabetic answer
def force_str(question):
    ans = input(question)
    while not(ans.lower().strip().isalpha()) or ' ' in ans.strip():
        print("Answer needs to be one word that only has letters.")
        ans = input(question)
    return ans

#Make sure the user types an int
def force_int(question):
    ans = input(question)
    while not ans.isdigit():
        print("Answer needs to be an integer.")
        ans = input(question)
    return ans

#-------------main routine--------------------
questions = [
    "How many letters are in the english alphabet, including upper and lower case letters? ",
    "What is the longest river in New Zealand? ",
    "What is the longest river in the world?",
    "What is the largest planet in the solar system? ",
    "What school do you go to? "
    ]

answers = [
    "26",
    "Waikato",
    "Nile",
    "Jupiter",
    "OBHS"
    ]

#Determines if the answer should be a word or a number
q_type = [force_int,force_str,force_str,force_str,force_str] 

print("Hello! This is a quiz.\nI will ask you 5 questions. Try to answer them correctly.") #greeting

#Quiz loop
score = 0
for q in range(len(questions)):
    ans = q_type[q](questions[q])
    if ans == answers[q]:
        print("Your answer is correct.")
        score += 1
    else:
        print("Your answer is incorrect.")

print(f"The quiz is over. You got {score} out of {len(questions)} questions right.")
