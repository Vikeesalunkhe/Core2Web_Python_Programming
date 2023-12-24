"""
9. Write a program to check whether the number is
Armstrong's number or not.
Input: 371
Output: 371 is Armsstrong’s number
"""
num2 = num1 = num = int(input("Enter value of num : "))
count = 0
Sum = 0

while num>0:
    num = num // 10
    count+=1

while num1>0:

    rem = num1 % 10
    Sum += rem**count
    num1 = num1//10

if Sum == num2:
    print(f"{num2} is Armsstrong number")

else:
    print(f"{num2} is not a Armsstrong number")

