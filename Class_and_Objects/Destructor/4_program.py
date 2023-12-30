class Parent:

    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20

    def disParent(self):
        print(self.x)
        print(self.y)

class Child(Parent):

    def __init__(self):
        print("In Child Parent")
        super().__init__()
        self.x = 30
        self.y = 40


obj = Child()
obj.disParent()




"""
O/p In Child Parent
    In Parent Constructor
    30
    40
"""


