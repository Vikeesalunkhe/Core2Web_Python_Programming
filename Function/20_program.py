#passing multiple variable of argument to a function

def fun(x,y,*argv):
    print(x)
    print(y)
    print(argv)


fun(10,20)

"""
O/p 10
    20
    ()

"""



