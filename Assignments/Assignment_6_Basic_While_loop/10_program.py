"""
10. WAP to print a cube of odd numbers up to n in reverse order.
Input: 15
Output: 3375 2197 1331 729 343 125 27 1
"""

num = int(input("Enter value of num : "))
i = 1

while (num>=i):
    if num % 2 == 1:
        print(num*num*num)
    num-=1
