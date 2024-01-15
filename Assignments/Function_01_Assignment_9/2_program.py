#What is the output of following function

def outer():
    def inner():
        return "Hello im the inner function"
    return inner

retobj = outer()
retinner = retobj()

print(retinner)


#O/p Hello im the inner function

