"""
8. Program 8: Write a program to check whether the number is greater than 10 or
not
Input: 12
Output: yes 12 is greater than 10
Input: 2
Output: no 2 is less than 10
"""

def Greater(x):

    if (x > 10):
        a = ("{} is greater than 10".format(x))
        return a

    else:
        b = ("{} is less than 10 ".format(x))
        return b
        

num = int(input("Enter the Value of num : "))
ret = Greater(num)
print(ret)
