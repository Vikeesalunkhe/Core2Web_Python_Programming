def outer():

    def inner():
        print("In inner function")
    
    print("In outer function")
    return inner


retObj = outer()                                #store return function address
retObj()                                        #function return in function (return function call)



"""
O/p In outer function
    In inner function
"""
