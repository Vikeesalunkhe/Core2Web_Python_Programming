#function decoretors

def decoFunc(Func):

    def wrapper():
        print("Start wrapper")
        Func()
        print("End wrapper")

    return wrapper

@decoFunc
def normalFunc():
    print("Hello in normal function")

normalFunc()

"""
O/p Start wrapper
    Hello in normal function
    End wrapper
"""

