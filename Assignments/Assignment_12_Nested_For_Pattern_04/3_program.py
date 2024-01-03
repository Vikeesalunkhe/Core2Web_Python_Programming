"""
Program3 : Row = 4
2 4 6 8
1 3 5 7
2 4 6 8
1 3 5 7
"""
rows = int(input("Enter Value of rows number : "))
num = 2
for i in range(rows):
    for j in range(rows):
        print(num, end =" ")
        num+=2

    print()
    if i % 2 == 0:
        num = 1

    else:
        num = 2
