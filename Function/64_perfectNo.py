'''
3. Write a program to check whether the number is a Perfect
number or not.
Input: 496
Output: 496 is a perfect number.
'''

def PerfectNo(num):

    Sum = 0
    for i in range(1,num//2+1):

        if num % i == 0:
            Sum+=i

    return Sum

x = int(input("Enter the value of num : "))
ret = PerfectNo(x)
if ret == x:
    print(f"{x} is perfect number ")

else:
    print("not a perfect no. ")
