#function return in function

def outer(x,y):

    def inner(a,b):
        print("In inner function")
        return a+b

        def inner2(x):
            print(x)
        
        return inner2
    print("In outer function")
    print(x+y)
    return inner


retObj = outer(5,8)
innerObj = retObj(3,4)

print(retObj)
print(innerObj)

"""
O/p  In outer function
     13
     In inner function
     <function outer.<locals>.inner at 0x7fb61f8abac0>
     7i

"""


