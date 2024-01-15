def outer():
    def inner():
        return outer

    return outer

if __name__=="__main__":
    retObj = outer()
    retInner = retObj()

    print(retInner)



#O/p <function outer at 0x7faf480abac0>

