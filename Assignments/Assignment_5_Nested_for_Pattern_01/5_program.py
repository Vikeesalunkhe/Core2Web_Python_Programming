"""
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
"""
def pattern(x):
    for i in range(4):
        num = 1+i
        for j in range(4):
            print(num,end = " ")
            num = num + 1

        print()


row = int(input("Enter the row value : "))
pattern(row)
