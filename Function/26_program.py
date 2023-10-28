#Nested Function

def outer():                                     #nested outer function

    def inner():                                 #nested inner function
        print("In ineer function")

    print("In outer function")
    inner()                                     #inner function call


outer()                                         #outer function call 



"""
O/p   In outer function
      In ineer function
"""
