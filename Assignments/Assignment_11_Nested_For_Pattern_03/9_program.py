"""
9.

E
E D
E D C
E D C B
E D C B A
"""

row = int(input("Enter Value of row no. : "))
for i in range(1,row+1):
    num = 69
    for j in range(i):
        print(chr(num), end = " ")
        num-=1

    print()

