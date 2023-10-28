#passing variable number of keyword argument to a function

def fun(x,y,**argv):
    print(type(argv))
    print(x)
    print(y)
    print(argv)


#fun(x = 10, p = 20, y = 30)
fun(x = 10,p = 20,y = 30)

"""
O/p 10
    30
    {'p': 20}

"""
