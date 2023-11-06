"""
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""

def fun(x):
    num = 1
    for i in range(x):
        for i in range(x):
            print(num,end = "\t  ")
            num = num + 1

        print()


row = int(input("Enter the row no size : "))
fun(row)
