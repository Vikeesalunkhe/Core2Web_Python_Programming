"""
6.
1 0 1 0 1
1 0 1 0
1 0 1
1 0
1
"""

row = int(input("Enter the Row No. : "))
for i in range(row,0,-1):
    for j in range(1,i+1):
        if j % 2 == 1:
            print("1", end = " ")

        else:
            print("0", end = " ")

    print()
