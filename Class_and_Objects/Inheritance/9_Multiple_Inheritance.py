class Parent1:

    def __init__(self):
        print("In Constructor:Parent 1")


class Parent2:

    def __init__(self):
        print("In Constructor:Parent 2")

class Child(Parent1, Parent2)i:                                                                #first Priority First Parent class
    pass


obj = Child()



#O/p In Constructor:Parent 1
