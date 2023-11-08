"""
1
3  5
7  9  11
13 15 17 19
"""

def pattern(x):

    i = 0
    num = x
    while(i<4):
        j = 0
        while(j<i+1):
            print(num,end = " ")
            j+=1
            num +=2

        print()
        i+=1

pattern(1)
