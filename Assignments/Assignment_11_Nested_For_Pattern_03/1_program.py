"""
Take number of rows from user

1
2 2
3 3 3
4 4 4 4
"""

num = int(input("Enter the NO. row : "))
for i in range(1,num+1):
    for j in range(i):
        print(i, end = " ")

    print()
