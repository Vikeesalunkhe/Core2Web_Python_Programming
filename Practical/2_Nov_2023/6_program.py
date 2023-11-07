"""
program_6:
    1 0 1 0 1
    1 0 1 0
    1 0 1
    1 0
    1
"""
Range = 5
for i in range(5):
    for j in range(Range):
        if j % 2== 0:
            print("1",end = " ")

        else:
            print("0",end = " ")

    print()
    Range-=1
