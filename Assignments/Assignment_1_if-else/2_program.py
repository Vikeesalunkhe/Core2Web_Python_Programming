#2. Program 2: Write a Program to check whether the number is Negative,Positive or equal to Zero.
#Input: -2
#Output: -2 is the negative number


num = int(input("Enter value of num : "))

if (num > 0):
    print("%d is the positive number"%num)

elif (num < 0):
    print("%d is the negative number"%num)

else:
    print("num is equal to zero")
