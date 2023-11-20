"""
Program 2: Write a Program to check whether the number is Negative,
Positive or equal to Zero.
Input: -2
Output: -2 is the negative number
"""

def negativeNo(x):

    if x < 0 :
        return ("{} is the negative number".format(x))

    elif  x == 0:
        return ("{} is the equal to zero".format(x))

    else:
        return ("{} is the positive number".format(x))


num = int(input("Enter the value of num : "))
retvalue = negativeNo(num)

print(retvalue)
