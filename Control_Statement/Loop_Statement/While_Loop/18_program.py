#pattern


row = int(input("Enter value of row : "))

num = 1
i = 1
while (row>=i):
    j = 1
    while (j<=row):
        print(num,end = " ")
        j+=1
        num +=1

    row -=1
    print()




"""
O/p

1 2 3
4 5
6

"""
