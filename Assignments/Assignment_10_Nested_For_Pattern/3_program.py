"""
Program3 : Rows = 4
A B C D
A B C D
A B C D
A B C D
"""


for i in range(4):
    num = 65
    for j in range(4):
        print(chr(num),end = " ")
        num+=1

    print()