"""
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
"""

def fun(x):
    num = 1
    for i in range(x):
        for j in range(x):
            print(num,end = " ")
        
        num = num + 1
        print()


row = int(input("Enter the row value : "))
fun(row)
