"""
7. Take two numbers from the user, check if both are odd and then print the
sum of the numbers.
#Input: num1 = 10
#Input: num2 = 11
#Output: 21
#Input: num1 = 10
#Input: num2 = 6
#Output: No Output
"""
def data():

    def CheakOdd(x,y):

        if (x % 2 ==1) and (y % 2 ==1):
            return (x+y)

        else:
            return ("not odd")
    return CheakOdd


num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))

ret1 = data()
ret2 = ret1(num1,num2)
print(ret2)

print(type(ret1))
print(type(ret2))
