"""
* * *
* * *
* * *
"""


def star(x):
    for i in range(x):
        for j in range(x):
            print("*",end = " ")

        print()




size_row_column = int(input("Enter size of row Value : "))
star(size_row_column)




