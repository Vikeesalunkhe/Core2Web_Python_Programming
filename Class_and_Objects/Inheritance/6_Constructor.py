class Parent:

    def __init__(self):
        print("In Constructor Parent")


class Child(Parent):

    def __init__(self):
        super().__init__()
        #Parent.__init__(self)
        #Parent()
        print("In Child Constructor")

    

obj1 = Child()


"""
O/p In Constructor Parent
    In Child Constructor
"""
