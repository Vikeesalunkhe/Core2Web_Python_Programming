"""

program_5:

    1 2 3 4
    1 2 3
    1 2
    1

"""
Range = 4
for i in range(4):
    num = 1
    for j in range(Range):
        print(num ,end = " ")
        num +=1

    Range-=1
    print()
