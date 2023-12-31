"""
Program10 : Row = 4
D4 C3 B2 A1
D4 C3 B2 A1
D4 C3 B2 A1
D4 C3 B2 A1
"""

for i in range(4):
    num = 68
    for j in range(4,0,-1):
        print(chr(num) + str(j), end = " ")
        num-=1

    print()
