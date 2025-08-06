'''
    author: myName
    date: 07/08/2025
    version: 1.0.0
    description: Prints happy birthday several times with as few lines of code as possible
'''

HB = "Happy birthday"
HBY = HB+" to you"
def repeat_print(args,times,s=' ',e='\n'):
    for i in range(times):
        print(args,sep=s,end=e)

for i in range(2):
    repeat_print(HBY,2)
    print(HB,HB)
    print(HBY,'\n')
repeat_print(HB,3)
print("to you",'\n')
repeat_print(HBY,2)
repeat_print(HB,2,e=' ')

