class Parent:

    def __init__(self):
        print("Parent Constructor")
        self.x = 10
        self.y = 20

    def disParent(self):
        print(self.x)
        print(self.y)

class Child(Parent):

    def __init__(self):
        print("In Child Constructor")
        self.x = 30
        self.y = 40
        super().__init__()


obj = Child()
obj.disParent()


"""
O/p In Child Constructor
    Parent Constructor
    10
    20
"""
