#print odd number between * 
 
x = int(input("Enter value of x :"))
i = 1
while (i<=x):

    if (i % 2 == 1):
        print(i, end = " ")

    else:
        print("*",end = " ")

    i += 1



#O/p 1 * 3 * 5 * 6 * ................


