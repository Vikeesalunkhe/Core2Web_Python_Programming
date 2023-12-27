
def fun(x,y):

    print("Start fun")
    while(x<=y):
        yield x
        x+=1

    print("End fun")

ret = fun(1,10)

print(next(ret))
print(next(ret))

for i in ret:
    print(i)



"""
O/p 
Start fun
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
End fun
"""
