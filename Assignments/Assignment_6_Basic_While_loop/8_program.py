"""
8. WAP to print the sum numbers up to n.
Input: 10
Output: sum of numbers upto 10 is 55
"""

num = int(input("Entee Value of sum of up to n no. : "))
i = 1
num_sum = 0

while i <= num:

    num_sum +=i
    i+=1

print("sum of numbers upto {} is {}".format(num,num_sum))
