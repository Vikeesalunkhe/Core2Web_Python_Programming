#Destructor

class Parent:

    z = 30
    def __init__(self):
        print("In Parent Constructor")
        self.x = 10
        self.y = 20

    def dispData(self):
        print(self.x)
        print(self.y)

    @classmethod
    def dispParent(cls):
        print(cls.z)

    def __del__(self):
        print("In Destructor")



obj = Parent()
obj = Parent()
print("End Code")


"""
O/p In Parent Constructor
    In Parent Constructor
    In Destructor
    End Code
    In Destructor
"""
