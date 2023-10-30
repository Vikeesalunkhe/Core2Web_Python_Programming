#pattern

row = int(input("Enter value of num : "))

i = 1
while (i <= row):
    j = 1
    while (j <= i):
        print("*", end = " ")
        j +=1

    print()
    i+=1


"""
O/p  
*
* *
* * *
* * * *

"""
