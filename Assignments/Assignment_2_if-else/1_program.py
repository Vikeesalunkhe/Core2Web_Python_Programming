"""
Q1 WAP to check numbers are divisible by 4 and 5 between a given range Print those numbers
Input1: num1 =20
Output:Numbers divisible by 4 and 5 are 20
Input1: num1 =15
Output:Numbers Not divisible by 4 and 5 are

"""

num1 = int(input("Enter Value of num1 : "))


if (num1 % 4 == 0) and (num1 % 5 == 0):
    print("divisible by 4 and 5 are  %d "%num1)

else:
    print("Not divisible by 4 and 5")
