"""
2. What is the output of the following function? (dry run compulsory)
def outer():
    def inner():
        return "Hello, I'm the inner function!"
    return inner

retObj = outer()
retInner = retObj()
print(retInner)
"""

def Outer():
    def inner():
        return "Hello, I,m the inner function!"
    return inner

retObj = Outer()
retInner = retObj()
print(retInner)





#O/p Hello, I,m the inner function!
