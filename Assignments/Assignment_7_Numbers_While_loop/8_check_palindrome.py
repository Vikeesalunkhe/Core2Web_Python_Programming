"""
8. Write a program to check whether the number is a
Palindrome number or not.
Input: 2332
Output: 2332 is a palindrome number
"""

num1 = num = int(input("Enter value of num : "))
rev = 0

while num>0:

    rem = num % 10
    rev = rev*10+rem
    num = num//10


if rev == num1:
    print("{} is a palindrome No.".format(num1))

else:
    print("{} is not a palindrome No. ".format(num1))
