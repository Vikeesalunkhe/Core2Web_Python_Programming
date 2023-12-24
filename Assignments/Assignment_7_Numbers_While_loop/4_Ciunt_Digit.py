"""
4. Write a program to count the digits of the given number.
Input:942111423
Output: 9
"""

num = int(input("Enter Value of num : "))
i = 1
count = 0

while num>0:

    num = num//10
    count+=1

print("Total no of digits : ",count)
