"""
# # # # #
@ @ @ @ @
# # # # #
@ @ @ @ @
# # # # #
"""

for i in range(1,6):

    if (i % 2 == 1):
        for j in range(1,6):
            print("#",end = " ")

        print()

    else:
        for j in range(1,6):
            print("@",end = " ")

        print()
