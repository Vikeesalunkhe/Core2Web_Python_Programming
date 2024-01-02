"""
10.

E F G H I
D E F G
C D E
B C
A
"""

row = int(input("Enter Value of row no. : "))
num = 69
for i in range(row,0,-1):
    for j in range(i):
        print(chr(num), end = " ")
        num+=1

    print()
    num-=i+1

        

