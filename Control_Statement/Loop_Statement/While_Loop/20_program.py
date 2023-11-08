"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

"""

def pattern(x):
    i = 0
    while(i<5):
        num = x
        j = 0
        while(j<i+1):
            print(num,end = " ")
            j+=1
            num-=1

        print()
        i+=1

pattern(5)
