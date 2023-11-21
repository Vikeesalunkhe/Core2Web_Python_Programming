"""
3. Take two numbers from users and print the sum of those numbers
if the sum is even.
Input1: num1 = 10
Input2: num2 = 20
Output: 30 is EvenInput1: num1 = 10
Input2: num2 = 15
Output: No Output
"""

def SumEven(x,y):

    numsum =  x+y
    if (numsum % 2 == 0):
        print(numsum,"is Even")
    else:
        print("not output")

num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))
SumEven(num1, num2)

