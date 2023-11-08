"""

1 1 1 1
2 2 2
3 3
4
"""

def pattern():
    i = 0
    num = 1
    while(i < 4):
        j = i
        while(j < 4):
            print(num , end = " ")
            j+=1

        print()
        i+=1
        num+=1

pattern()
