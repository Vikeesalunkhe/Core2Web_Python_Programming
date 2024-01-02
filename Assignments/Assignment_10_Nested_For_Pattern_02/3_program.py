"""
Program3 : Rows = 4
A B C D
A B C D
A B C D
A B C D
"""
rows = int(input("Enter Value of rows no. : "))

for i in range(rows):
    num = 65
    for j in range(rows):
        print(chr(num),end = " ")
        num+=1

    print()
