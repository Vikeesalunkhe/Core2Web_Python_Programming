"""
E F G H I
D E F G 
C D E 
B C 
A
"""

num = 69
temp = 6
i = 0
while(i<5):
    j = i
    while(j<5):
        print(chr(num),end = " ")
        num+=1
        j+=1

    print()
    num = num - temp
    temp-=1
    i+=1

