#check even or odd no in input range


x = int(input("Enter Value of x :"))
y = int(input("Enter value of y :"))


for i in range(x, y+1):

    if (i % 2 == 0):

        print("{} is even".format(i))

    else:

        print("{} is odd".format(i))



