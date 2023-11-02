#Function return in Function

def outer():

    def inner1():
        print("In ineer1 function")

    def inner2():
        print("In inner2 function")

    return inner1,inner2

#retObj = outer()
innr1, innr2 = outer()            #store multiple return function 

#print(innr1)                     #print address of def inner1
#print(innr2)                     #print address of def inner2

innr1()
innr2()

"""
O/p In ineer1 function
    In inner2 function
"""



