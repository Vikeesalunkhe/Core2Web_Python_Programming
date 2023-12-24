"""
7. Write a program to reverse the given number.
Input:43521
Output: 12534
"""

num = int(input("Entyer value of num : "))
Rev = 0
while num>0:
    rem = num % 10
    Rev = Rev*10+rem
    num = num // 10

print(Rev)
