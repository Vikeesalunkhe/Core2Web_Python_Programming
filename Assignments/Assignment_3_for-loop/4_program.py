"""
4. Write a program to print even numbers 1-100
"""

def even(start,end):
    for i in range(start ,end):
        if (i % 2 == 0):
            print("{} is even number".format(i))

even(start = 1,end = 100)
