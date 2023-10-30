#pattern

row = int(input("Enter value of num : "))

num = 65
i = 1
while (i<=row):
    j = 1
    while (j<=i):
        print(chr(num),end = " ")
        j +=1
        num = num + 1

    print()
    i +=1



"""
O/p

A
B C
D E F
G H I J

"""
