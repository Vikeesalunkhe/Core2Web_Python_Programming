"""
1. What is the output of the following function?
"""

def outer():
    def inner():
        return "Hello im the inner function"

    return inner()

ans = outer()
print(ans)



#O/p Hello im the inner function

