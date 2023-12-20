"""
7. WAP defines a class Sum with a mySum method that returns the sum of two numbers.
The program creates two class objects, takes user input to set values for each object,prints the return sum for both objects, and then determines whether the total sum is even
or odd.
"""
class Sum:

    def mySum(self,x,y):
        return x + y

Obj1 = Sum()
Obj2 = Sum()

num1 = int(input("Enter Value of num1 : "))
num2 = int(input("Enter Value of num2 : "))

Sum1 = Obj1.mySum(num1, num2)

num3 = int(input("Enter value of num3 : "))
num4 = int(input("Enter Value of num4 : "))

Sum2 = Obj2.mySum(num3, num4)

total_sum = Sum1 + Sum2

if total_sum % 2 == 0:
    print("total sum is Even")

else:
    print("total sum is Odd")

