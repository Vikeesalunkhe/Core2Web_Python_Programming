def decorFun(Func):

    def wrapper():
        print("start wrapper_1")
        Func()
        print("End wrapper_1")

    return wrapper


def decorRun(Func):

    def wrapper():
        print("Start wrapper_2")
        Func()
        print("End wrapper_2")

    return wrapper

def normalFun():
    print("In normal fun")

ret = decorFun(decorRun(normalFun))
ret()


"""
O/p start wrapper_1
    Start wrapper_2
    In normal fun
    End wrapper_2
    End wrapper_1
"""

