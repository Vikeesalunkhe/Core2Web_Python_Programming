"""
1. WAP to print the following series using a while loop
105, 98, 91, 84, 77, 70 ........7
"""

def Series(num):

    i = 1
    while num>=1:
        print(num, end = " ")
        num-=7



num = int(input("Enter value of num : "))
Series(num)
