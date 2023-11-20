"""
4. Program 4: Write a Program to check whether the number is divisible by 5
or not.
Input: 55
Output: 55 is divisible by 5
"""

def Divisible(x):

    if (x % 5 == 0):
        return ("%d is Divisible by 5"%x)

    else:
        return ("%d is not Divisible by 5"%x)



num = int(input("Enter the Value of num : "))

ret1 = Divisible(num)

print(ret1)
print(type(ret1))
