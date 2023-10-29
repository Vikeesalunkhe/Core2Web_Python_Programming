#print 5 * 15 * 25 * 35 * 45 * ....

num = int(input("Enter Value of num : "))
i = 1
while (i<=num):

    if (i % 5 == 0) and (i%2 == 0):
        print("*",end = " ")

    elif ( i % 5 == 0):
        print(i,end = " ")
    

    i+=1



#O/p  5 * 15 * 25 * 35 * 45 * 55 *
