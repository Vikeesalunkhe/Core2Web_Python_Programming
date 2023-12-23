
def decorFun(Func):

    def wrapper():
        print("Satart wrapper")
        Func()
        print("End wrapper")

    return wrapper

def normalFun():
    print("In normal fun")


ret = decorFun(normalFun)
ret()
