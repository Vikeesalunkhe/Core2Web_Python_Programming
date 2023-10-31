"""
9. Write a program to print the sum of the first 10 numbers
"""

def SumTen(num):

    Sum = 0
    for i in range(1,num+1):
        Sum += i

    return Sum




num = int(input("sum of 1 to   :"))
ret = SumTen(num)
print(ret)



#O/p 55
