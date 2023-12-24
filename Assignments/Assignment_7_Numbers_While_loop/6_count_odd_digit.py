"""
6. Write a program to count the Odd digits of the given
number.
Input: 942111423
Output: 5
"""
num = int(input("Enter value of num : "))
count = 0

while num>0:

    rem = num % 10
    if rem % 2 == 1:
        count+=1

    num = num//10

print("total odd digit count is ",count)
