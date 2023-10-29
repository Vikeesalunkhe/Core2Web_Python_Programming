#print even nu. in letter character and even is number

num = int(input("Enter Value of num  : "))

i = 1
while (i<=num):

    if (i % 3 == 0):
        print("three")

    elif (i % 5 == 0):
        print("five")

    else:
        print(i)

    i+=1

"""
O/p
1
2
three
4
five
three
7
8
three
five
"""
