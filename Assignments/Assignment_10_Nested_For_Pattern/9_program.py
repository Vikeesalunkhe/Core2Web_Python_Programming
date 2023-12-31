"""
Program9: Row = 3
A b C
d E f
G h I
"""
Upper = 65
Lower = 97
for i in range(3):

    for j in range(3):
        if Upper % 2 == 1:
            print(chr(Upper), end = "  ")

        else:
            print(chr(Lower), end = "  ")
        Upper+=1
        Lower+=1

    print()
