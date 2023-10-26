"""
7. Take two numbers from the user, check if both are odd and then print the sum of the numbers.
#Input: num1 = 10
#Input: num2 = 11
#Output: 21
#Input: num1 = 10
#Input: num2 = 6
#Output: No Output

"""

num1 = int(input("Enter Value of num2 :"))
num2 = int(input("Enter value of num2 :"))

if (num1 % 2 == 1) and (num2 % 2 == 1):
    _sum = num1 + num2
    print(_sum)

else:
    print("No Output")
