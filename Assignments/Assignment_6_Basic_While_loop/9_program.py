"""
9. WAP to print squares of even numbers up to n.
Input: 10
Output: 4 16 36 64 100.
"""

num = int(input("Enter Value of num : "))
i = 1

while (i <= num):
    if i % 2 == 0:
        print(i*i,end = " ")
    i+=1




