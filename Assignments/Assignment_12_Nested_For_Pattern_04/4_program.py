"""
Program4 : Row = 4
1  3  5  7
7  10 13 16
16 20 24 28
28 33 38 43
"""
rows = int(input("Enter value of rows number : "))
num = 1
for i in range(1,rows+1):
    for j in range(rows):
        print(num, end  = "\t")
        num+=i+1

    print()
    num=num-(i+1)


