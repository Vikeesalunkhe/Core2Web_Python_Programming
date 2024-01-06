class Parent1:

    def __init__(self):
        print("In Parent 1")

    def Data1(self):
        print("In Parent1 Data")

class Parent2:

    def __init__(self):
        print("In parent 2")
        self.x = 10

    def Data2(self):
        print("In Parent2 Data")

class Child(Parent1, Parent2):

    def __init__(self):
        print("In Child")
        self.y = 20
        Parent2.__init__(self)
        print(self.y)
        print(self.x)


obj = Child()
obj.Data1()
obj.Data2()



'''
O/p In Child
    In parent 2
    20
    10
    In Parent1 Data
    In Parent2 Data
'''
