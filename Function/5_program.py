#check given no is divisible by 4 and 5 and print using def-if-else function

def divisible(x):
    
    if (x % 4 == 0) and (x % 5 == 0):
        print("{} is divisible by 4 and 5".format(x))

    else:
        print("{} is Not Divisible by 4 and 5".format(x))

num = int(input("Enter Value of num : "))
divisible(num)
