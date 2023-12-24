"""
5. Write a program to count the even digits of the given
number.
Input: 942111423
Output: 4
"""
num = int(input("Enter value of num : "))
count = 0
while num>0:

    rem = num%10
    if rem % 2 == 0:
        count+=1

    num = num // 10

print("Even digit count is ",count)
