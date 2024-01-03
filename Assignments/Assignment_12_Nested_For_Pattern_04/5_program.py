"""
Program5 : Rows = 3
1  2   4
8  16  32
64 128 256
"""

rows = int(input("Enter Value of rows number : "))
num = 1
for i in range(rows):
    for j in range(rows):
        print(num, end = "\t")
        num+=num

    print()
