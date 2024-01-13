'''
7. WAP defines a class Sum with a mySum method that returns the sum of two numbers.
The program creates two class objects, takes user input to set values for each object,
prints the return sum for both objects, and then determines whether the total sum is even
or odd.
Input:
Object1 input:
Num1 = 3
Num2 = 5
Object input:
Num1= 4
Num2 = 5

Output: Sum is Odd 17
'''

class Sum:

    def mySum(self, num1, num2):

        return num1+num2


num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))
obj1 = Sum()
ret1 = obj1.mySum(num1, num2)


num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))
obj2 = Sum()
ret2 = obj2.mySum(num1, num2)

add = ret1+ret2

if  add % 2 == 1:
    print(f"sum id odd {add}")

else:
    print(f"sum id even {add}")


