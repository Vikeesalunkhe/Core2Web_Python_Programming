#function return in function

def outer():

    def inner1():
        print("In inner1 function")

    def inner2():
        print("In inner2 function")

    return inner1, inner2


retObj = outer()

for i in retObj:
    i()


"""
O/p  In inner1 function
     In inner2 function
"""
