"""
program_10:

    E F G H I
    D E F G
    C D E 
    B C 
    A
"""
num = 69
for i in range(5,0,-1):
    for j in range(i):
        print(chr(num),end = " ")
        num = num + 1

    print()
    num-=i+1
