##Decoretor Chaining

def decorFun(Func):

    def wrapper():
        print("Start wrapper2")
        Func()
        print("End wrapper2")

    return wrapper

def decorRun(Func):

    def wrapper():
        print("Start wrapper1")
        Func()
        print("End wrapper1")

    return wrapper

@decorFun
@decorRun
def normalFun():
    print("IN normal fun")


normalFun()


"""
O/p Start wrapper2
    Start wrapper1
    IN normal fun
    End wrapper1
    End wrapper2

"""
