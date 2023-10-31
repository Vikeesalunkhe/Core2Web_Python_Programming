"""
5. Write a program to print odd numbers 1-50
"""
def Odd(start ,end):
    for i in range(start,end):
        if (i % 2  == 1):
            print("%d is odd number"%i)


Odd(start = 1 ,end = 50)
