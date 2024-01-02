"""
Program2 : Rows = 3
A B C
D E F
G H I
"""
rows = int(input("Enter value of rows no. : "))

num = 65
for i in range(rows):
    for j in range(rows):
        print(chr(num), end = "\t ")
        num+=1

    print()
