"""
Program6 : Rows = 4
1  4  7  10
2  5  8  11
3  6  9  12
4  7  10 13
"""
for i in range(1,5):
    num = i
    for j in range(4):
        print(num,end = "\t")
        num+=3

    print()
