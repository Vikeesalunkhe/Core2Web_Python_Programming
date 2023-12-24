"""
10. Write a program to check whether the number is a Strong
number or not.
Input: 145
Output: 145 is Strong number
"""
num1 = num = int(input("Enter value of num : "))
Sum = 0

while num>0:
    
    fact = 1
    rem = num % 10
    while rem>0:
        fact = fact*rem
        rem-=1

    Sum = Sum + fact
    num = num//10

if Sum == num1:
    print(f"{num1} is Strong number")

else:
    print(f"{num1} is not a Strong number")
    
