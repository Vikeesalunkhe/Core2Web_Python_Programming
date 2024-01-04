"""
Program9 : Row = 4
1D 2C 3B 4A
1D 2C 3B 4A
1D 2C 3B 4A
1D 2C 3B 4A
"""
rows = int(input("Enter Value of rows number : "))
num = 68
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(chr(68)+str(j), end = " ")
        num-=1

    print()
    num = 68
