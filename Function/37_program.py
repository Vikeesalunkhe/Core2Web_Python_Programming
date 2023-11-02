#function return in function

def outer():
    def inner1(x,y):
        print("In inner1 function")
        return x+y

    def inner2(a,b):
        print("In inner2 finction")
        return a*b

    return inner1,inner2


inn1,inn2 = outer()

ret1 = inn1(10,20)
ret2 = inn2(3,4)

print(ret1 + ret2)
print(ret1)
print(ret2)


"""
O/p  In inner1 function
     In inner2 finction
     42
     30 
     12

"""
        
