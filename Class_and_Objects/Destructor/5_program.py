class Demo:

    def __init__(self):
        print("In Constructor")

    def __del__(self):
        print("In Destructor")


obj1 = Demo()
obj2 = Demo()



"""
O/p In Constructor
    In Constructor
    In Destructor
    In Destructor
"""

