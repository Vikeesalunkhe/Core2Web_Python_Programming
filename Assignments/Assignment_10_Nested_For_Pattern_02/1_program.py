"""
Nested for Patterns_02
Program1 : Rows = 3
1  4  9
16 25 36
49 64 81
"""
rows = int(input("Enter Value of rows number : "))
num = 1
add = 3

for i in range(rows):
    for j in range(rows):
        print(num, end = "\t")
        num +=add
        add+=2 

    print()
