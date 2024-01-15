def outer():
    def inner(a,b):
        print("in inner1")
        return a-b

    def inner2(obj):
        print("in inner2")
        print(obj)
        return inner2

    retinner1 = inner(10,4)
    retinner2 = inner2(retinner1)
    return retinner2

if __name__=="__main__":
    retObj = outer()
    print(retObj)


'''
O/p 
in inner1
in inner2
6
<function outer.<locals>.inner2 at 0x7f92a92ebeb0>
'''
