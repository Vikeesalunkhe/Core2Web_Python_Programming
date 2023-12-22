def decorFun(Func):

    print("In decor Func")

    def wrapper(*argv):
        print("Start wrapper")
        val = Func(*argv)
        print("End wrapper")
        return val

    return wrapper

@decorFun
def normalFun(x,y):
    print("In normal fun")
    return x+y

print(normalFun(10,20))



"""
O/p In decor Func
    Start wrapper
    In normal fun
    End wrapper
    30
"""
