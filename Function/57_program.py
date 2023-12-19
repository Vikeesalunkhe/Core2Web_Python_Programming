def fun():

    def inner1():
        return "inner1"

    def inner2():
        return "inner2"

    return inner1,inner2

retfun = fun()

for x in retfun:
    print(x())
