"""
Nested for Patterns_02
Program1 : Rows = 3
1  4  9
16 25 36
49 64 81
"""

num = 1
add = 3
for i in range(3):
    for j in range(3):
        print(num, end = "\t")
        num+=add

    print()
