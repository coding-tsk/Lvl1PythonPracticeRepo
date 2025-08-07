'''
    author: MyName
    date: 08/08/2025
    version: 1.0.0
    description: Get five numbers and store them in a list
'''
#-------------libraries------------------

#------------functions-----------------
def average(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum/len(nums)
#------------main routine----------------
if __name__ == "__main__":
    nums = [int(l) for l in input("Enter 5 numbers seperated by a comma: ").split(',')]
    print("These are your numbers:",end=" ")
    for n in nums[:-1]:
        print(n,end=",")
    print(nums[-1])

    print("The average of your numbers is:",average(nums))
    print("The rounded average is: ",round(average(nums)))
    