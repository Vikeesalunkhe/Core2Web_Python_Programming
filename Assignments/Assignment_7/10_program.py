"""
10. Write a program in which you have to write a __new__ user-defined function that
creates a new instance of a class.
"""

class Demo:

    def __new__(self):
        print("New Instance Function")
        return super().__new__(self)

    def __init__(self):
        print("In Constructor")

Obj = Demo()



'''
O/p New Instance Function
    In Constructor
'''
