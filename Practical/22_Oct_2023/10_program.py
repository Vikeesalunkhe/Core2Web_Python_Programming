"""
write a program to print no. that are divided by take range from user and no. print that divided by 4 and not divided by 5
I/p  x = 1
     y = 50
"""



x = int(input("Enter value of x :"))
y = int(input("Enter Value of y :"))


for i in range(x, y+1):

    if (i % 4 == 0) and (i % 5 != 0):

        print(i)
