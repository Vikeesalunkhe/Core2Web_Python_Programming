"""
Program2 : Rows = 3
A B C
C D E
E F G
"""
num = 65
for i in range(3):
    for j in range(3):
        print(chr(num), end = " ")
        num+=1

    print()
    num-=1

