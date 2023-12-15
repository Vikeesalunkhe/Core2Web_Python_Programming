#constructor

class Demo:

    def __new__(self):
        print("In new")
        return super().__new__(self)

    def __init__(self):
        print("In constructor")

obj = Demo()

"""
O/p  In new
     In constructor

"""

