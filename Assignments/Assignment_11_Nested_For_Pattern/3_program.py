"""
3.

1
3  5
7  9  11
13 15 17 19
"""

row = int(input("Enter value of ROW no. : "))
num = 1
for i in range(1,row+1):
    for j in range(i):
        print(num, end = "\t")
        num+=2

    print()
