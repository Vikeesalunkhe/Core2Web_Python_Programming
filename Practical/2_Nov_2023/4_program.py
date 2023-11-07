"""
program_4:

    1 1 1 1 
    2 2 2
    3 3
    4

"""

num = 1
for i in range(4,0,-1):
    for j in range(i):
        print(num ,end = " ")

    num = num + 1
    print()
