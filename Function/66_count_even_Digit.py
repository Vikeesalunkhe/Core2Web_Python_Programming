'''
Write a program to count the even digits of the given
number.
Input: 942111423
Output: 4
'''

def EvenDigit(num):

    count = 0
    while 1<=num:

        rem = num%10
        if rem % 2 == 0:
            count+=1

        num = num//10

    return count

x = int(input("Enter value of num : "))
ret = EvenDigit(x)
print("Total Even no. of digit is : ",ret)
