#Nested function


def outer():

    def inner1():
        print("In inner1 function")

    inner2()                                                      ##
    def inner2():
        print("In inner2 function")

    print("In outer function")


outer()


#O/p  UnboundLocalError: local variable 'inner2' referenced before assignment


