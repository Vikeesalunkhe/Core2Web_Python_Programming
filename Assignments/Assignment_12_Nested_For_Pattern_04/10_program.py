"""
Program10 : Rows = 4
A  2  C  4
A  6  C  8
A  10 C  12
A  14 C  16
"""

rows = int(input("Enter Value of rows number : "))
num = 65
Sum = 2
for i in range(1,rows+1):
    for j in range(1,rows+1):

        if (j % 2 == 1):
            print(chr(num), end = "\t")
            num+=2

        else:
            print(Sum, end = "\t")
            Sum+=2

    print()
    num = 65
