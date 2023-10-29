#pattern using while loop


row_column = int(input("Enter value of row and column : "))
num = 1
i = 1
while (i<=row_column):
    j = 1
    while (j<=row_column):
        print(num,end = " ")
        j+=1
        num = num +1
    print()
    i+=1



"""
O/p 1 2 3
    4 5 6
    7 8 9

"""
