'''
    author: name
    date: 8/8/2025
    version: 1.0.0
    description: a command line calculator
'''
#-----------libraries--------------------
import math
#--------------functions-------------------
#addition function
def add(n1,n2):
    return n1 + n2
#subtraction function
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        return "NA"
#--------------main routine-----------------
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
op = input("Enter your operation(+ - * /): ")
res = 0 #result of the operation

#choose operation based on op variable
if op == '+':
    res = add(num1,num2)
elif op == '-':
    res = sub(num1,num2)
elif op == '*':
    res = mult(num1,num2)
elif op == '/':
    res = div(num1,num2)
else:
    print(op,"is not a valid operation")
    res = "NA"

print("The result is:",res)