"""
1 2 3 4
1 2 3
1 2
1
"""

def pattern():
    i = 0
    while(i<4):
        j = i
        num = 1
        while(j<4):
            print(num,end = " ")
            j+=1
            num+=1

        print()
        i+=1

pattern()
