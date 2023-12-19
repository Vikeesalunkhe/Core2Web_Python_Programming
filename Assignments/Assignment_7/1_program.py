"""
1. What is the output of the following function?
def outer():
    def inner():
        return "Hello, I'm the inner function!"
    return inner()
ans = outer()
print(ans)
"""

def Outer():
    def inner():
        return "Hello, I,m the inner function"
    return inner()

ans = Outer()
print(ans)

"""
O/p  Hello, I'm the inner function!
"""
