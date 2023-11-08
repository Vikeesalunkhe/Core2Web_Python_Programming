"""
1 
3  2
6  5  4
10 9  8  7
"""

num = 1
i = 0
while(i < 4):
    j = 0
    while(j < i+1):
        print(num-j,end = " ")
        j+=1

    print()
    num = num+i+2
    i+=1


