def outer(x,y):

    while (x<=y):
        yield x
        x+=1

for i in outer(1,11):
    print(i)


"""
O/p
1
2
3
4
5
6
7
8
9
10
11
"""
