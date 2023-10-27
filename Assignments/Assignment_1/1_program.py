
#1. Program 1: Write a Program to Find a Maximum between two numbers
#Input: 1 2
#Output: 2 is Max number between 1 & 2


num1 = int(input("Enter Value of num1 : "))
num2 = int(input("Enter value of num2 : "))

if (num1 > num2):
    print("{} is Max number between {} and {}".format(num1,num1,num2))

else:
    print("{} is max number between {} and {}".format(num2,num1,num2))


