"""
6. WAP to print the table of entered number
Input: 10
Output:
10 20 30 40 50 60 70 80 90 100
Note : print the table in single line
"""

table_num = int(input("Enter Value of table_no : "))
i = 1

while i<=10:

    print(table_num * i,end =  " ")
    i+=1
