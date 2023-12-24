"""
3. Write a program to check whether the number is a Perfect
number or not.
Input: 496
Output: 496 is a perfect number.
"""
num = int(input("Ebter Value of num : "))
i = 1
Sum = 0
while i<=num/2:

    if num % i == 0:
        Sum+=i

    i+=1

if (Sum == num):
    print("{} is perfect No. ".format(num))

else:
    print("{} is a not perfect No.".format(num))
