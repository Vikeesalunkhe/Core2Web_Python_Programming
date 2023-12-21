def decoFun(Func):

    def wrapper():
        print("Start in wrapper")
        Func()
        print("End in wrapper")

    return wrapper

def normalFun():
    print("Hello, in normalFun")

ret = decoFun(normalFun)
ret()

"""
O/p Start in wrapper
    Hello, in normalFun
    End in wrapper
"""

