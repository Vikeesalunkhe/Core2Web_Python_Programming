#nested function

def outer():

    def inner1():
        print("In inner1 function")
    
    inner1()
    def inner2():
        print("In inner2 function")

    print("In outer function")


outer()


"""
O/p  In inner1 function
     In outer function
"""

