"""
4.

1 1 1 1
2 2 2
3 3
4
"""

row = int(input("Enter Value of row no. : "))
for i in range(1,row+1):
    for j in range(1,row+1):
        print(i, end = " ")

    row-=1
    print()

