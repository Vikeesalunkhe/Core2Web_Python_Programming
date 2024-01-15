def outer(flag):
    def inner():
        return "This is true." if flag else "This is false"

    return inner

if __name__=="__main__":
    retobj = outer(1)
    ret2 = retobj()
    print(ret2)



