"""
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""

def pattern(x):
    for i in range(x):
        num = 1
        for j in range(x):
            print(num,end = " ")
            num +=1

        print()


row = int(input("Enter the row value : "))
pattern(row)
