"""
program_7:

    1
    2  3
    3  4  5
    5  6  7  8
    8  9  10 11 12

"""

num = 1
for i in range(5):
    for j in range(i+1):
        print(num,end = "\t")
        num +=1

    print()
    if num == 2:
        pass
    else:
        num-=1
