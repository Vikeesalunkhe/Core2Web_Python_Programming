"""
8.

1
3  2
6  5  4
10 9  8  7
"""
row = int(input("Enter Value of row number : "))
num = 1
add = 3
for i in range(1,row+1):

    for j in range(i):
        print(num, end = "\t")
        num-=1

    num+=add
    add+=2
    print()
