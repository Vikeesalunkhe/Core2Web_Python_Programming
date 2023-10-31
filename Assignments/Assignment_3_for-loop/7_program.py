"""
7. Write a program to print a table of 12
"""
def Table(x,y):
    for i in range(1,x+1):
        print(y * i)


table_no = int(input("Enter table no value : "))        
Table(10,table_no)


"""
O/p

12
24
36
48
60
72
84
96
108
120

"""
