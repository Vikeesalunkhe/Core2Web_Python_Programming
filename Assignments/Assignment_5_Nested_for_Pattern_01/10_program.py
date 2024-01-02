"""
Program10 :
Row = 4
1  3  5  7
5  7  9  11
9  11 13 15
13 15 17 19
"""

row = int(input("Enter the row value : "))

for i in range(1,15,4):
    num = i
    for j in range(row):
        print(num, end = "\t ")
        num += 2

    print()
