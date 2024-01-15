def outer():
    def inner():
        return "Hello"

    return inner
    print("In Outer Function")

if __name__=="__main__":
    result = outer()
    print(result)







'''
O/p  <function outer.<locals>.inner at 0x7f9dccbefe20>
'''
