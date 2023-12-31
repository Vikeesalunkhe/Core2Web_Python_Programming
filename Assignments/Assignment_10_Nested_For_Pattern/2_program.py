"""
Program2 : Rows = 3
A B C
D E F
G H I
"""
num = 65
for i in range(3):
    for j in range(3):
        print(chr(num), end = "\t ")
        num+=1

    print()
