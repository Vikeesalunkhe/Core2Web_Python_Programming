"""
Program8: Row = 4
1   2   3   4
25  36  49  64
9   10  11  12
169 196 225 256
"""
rows = int(input("Enter Value of rows number : "))
num = 1

for i in range(1,rows+1):
    for j in range(1,rows+1):

        if i % 2 == 1:
            print(num, end = "\t")
            num+=1

        else:
            print(num*num, end = "\t")
            num+=1

    print()



