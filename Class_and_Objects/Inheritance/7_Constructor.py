class Parent:

    def __init__(self):
        print("In Parent Constructor")

    def parentFun(self):
        print("In parent Fun")

class Child(Parent):

    def __init__(self):
        super().__init__()
        #Parent.__init__(self)
        #Parent()
        print("In child Constrctor")

    def childFun(self):
        print("In child Fun")



obj1 = Child()
obj1.parentFun()
obj1.childFun()



"""
O/p In Parent Constructor
    In child Constrctor
    In parent Fun
    In child Fun
"""


