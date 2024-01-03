"""
Program1 : Rows = 3
0  3  8
15 24 35
48 63 80
"""

rows = int(input("Enter value of rows no. : "))

num = 0
add = 3
for i in range(rows):
    for j in range(rows):
        print(num, end  = "\t ")
        num = num + add
        add+=2

    print()

