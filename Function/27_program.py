#Nested function

def outer():

    def inner1():
        print("In inner1 function")

    def inner2():
        print("In inner2 function")

    
    print("In outer function")
    inner1()
    inner2()

outer()


"""
O/p  In outer function
     In inner1 function
     In inner2 function

"""


