"""
8. Write a program to print a table of 12 in reverse order

"""

def ReversTable(x):
    for i in range(10,0,-1):
        print(x * i)


Table_no = int(input("Enter table no. value : "))
ReversTable(Table_no)


"""
O/p
120
108
96
84
72
60
48
36
24
12
"""
