"""
program_8:
    1
    3  2
    6  5  4
    10 9  8  7
"""

num = 1
for i in range(4):
    for j in range(i+1):
        print(num-j,end = " ")
        

    print()
    num = num + i + 2
