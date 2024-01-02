"""
Program8 :
Row = 3
1 3 5
1 3 5
1 3 5
"""

row = int(input("Enter the row value : "))


for i in range(row):
    num = 1
    for j in range(row):
        print(num ,end = "\t ")
        num += 2

    print()
