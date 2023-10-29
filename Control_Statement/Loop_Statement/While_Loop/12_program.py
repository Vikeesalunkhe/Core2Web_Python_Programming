#pattern using while loop


row_column = int(input("Enter valu of row_column : "))
i = 1
num = 1
while (i<=row_column):

    j = 1
    while (j<=row_column):
        print(num,end = " ")
        j+=1

    num +=1
    i +=1
    print()



"""
P/p  1 1 1
     2 2 2
     3 3 3

"""
