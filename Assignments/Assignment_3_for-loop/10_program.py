"""
10. Write a program to print the product of the first 10 numbers
"""


def Product(x):
    prodt = 1
    for i in range(1,x+1):
        prodt *= i

    return prodt


num = int(input("Enter value of num : "))
ret = Product(num)
print(ret)





#O/p 3228800    (1 to 10 product)
