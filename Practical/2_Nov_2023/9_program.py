"""
program_9:

    E 
    E D
    E D C
    E D C B
    E D C B A
"""

for i in range(5):
    num = 69
    for j in range(i+1):
        print(chr(num),end = " ")
        num-=1

    print()
