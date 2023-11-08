"""
1
2  3
3  4  5
5  6  7  8
8  9  10 11 12
"""

def pattern():
    i = 0
    num = 1
    while(i < 5):
        j = 0
        while(j < i+1):
            print(num,end = "\t")
            j+=1
            num+=1

        print()
        i+=1
        if (num==2):
            pass
        else:
            num-=1

pattern()
