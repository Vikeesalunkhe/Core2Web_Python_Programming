"""
Assignment 2
1. WAP to check numbers are divisible by 4 and 5
Print those numbers
Input1: num1 =20
Output:
20 is divisible by 4 and 5
Input1: num1 =15
Output:
15 is not divisible by 4 and 5
"""

def Divisible(x):

    if (x % 4 == 0) and (x % 5 == 0):
        return ("%d is divisible by 4 and 5"%x)
    else:
        print("{} is not divisible by 4 and 5".format(x))

num =  int(input("Enter value of num : "))
ret = Divisible(num)
print(ret)
