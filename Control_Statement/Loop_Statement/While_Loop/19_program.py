"""
1 
2 2
3 3 3
4 4 4 4
"""

i = 0
num = 1
while(i<4):
    j = 0
    while(j<i+1):
        print(num,end = " ")
        j+=1

    print()
    i+=1
    num +=1


