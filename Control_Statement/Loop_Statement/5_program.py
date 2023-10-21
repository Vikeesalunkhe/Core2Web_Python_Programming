#check divisible by 4 and 5 in 1 to 100


x = int(input("Enter value of x :"))
y = int(input("Enter Value of y :"))

for i in range(x, y+1):

    if (i % 4 == 0) and (i % 5 == 0):

        print(i)
