"""
Program4 : Row = 3
2  5  10
17 26 37
50 65 82
"""
rows = int(input("Enter Value of rows no. : "))

num = 2
data = 3
for i in range(rows):
    for j in range(rows):
        print(num,end = "\t")
        num = num+data
        data+=2

    print()
