"""
4. WAP to calculate the factorial of a given number.
Input:
5
Output:
Factorial of 5 is 120
"""

num = int(input("Enter factorial no. : "))
fact = 1
i = 1

while i<=num:
    fact = fact * i
    i+=1

print("Factorial of {} is {}".format(num,fact))
