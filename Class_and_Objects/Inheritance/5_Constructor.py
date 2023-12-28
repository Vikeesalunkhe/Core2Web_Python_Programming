class Parent:

    def __init__(self):
        print("In constructor")

    def parentFun(self):
        print("In parent Fun")

class Child(Parent):
    pass


obj1 = Child()
obj1.parentFun()


"""
O/p In constructor
    In parent Fun
"""
