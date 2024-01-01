"""
7.

1
1 2
2 3 4
4 5 6 7
7 8 9 10 11
"""

row = int(input("Enter Value of row number : "))

num = 1
for i in range(1,row+1):
    for j in range(i):
        print(num, end = " ")
        num+=1

    print()
    num-=1
