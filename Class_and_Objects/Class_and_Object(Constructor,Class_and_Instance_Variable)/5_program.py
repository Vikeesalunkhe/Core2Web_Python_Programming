class Demo:

    def __new__(self):
        print("In new")
        return object.__new__(self)

    def __init__(self):
        print("In init")

obj = Demo()

"""
O/p In new
    In init
"""
