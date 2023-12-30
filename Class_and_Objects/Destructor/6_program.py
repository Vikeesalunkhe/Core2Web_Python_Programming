class Demo:

    def __init__(self):
        print("IN Constructor")


    def __del__(self):
        print("In Destructor")

obj1 = Demo()
obj2 = Demo()
obj3 = obj1
del obj1
print("End Code")



"""
O/p IN Constructor
    IN Constructor
    End Code
    In Destructor
    In Destructor
"""
