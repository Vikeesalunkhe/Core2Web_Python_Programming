"""
program_3:

    1
    3  5
    7  9  11
    13 15 17 19

"""

num = 1
for i in range(4):
    for j in range(i+1):
        print(num, end = "\t ")
        num = num + 2

    print()
    #num = num + 2
