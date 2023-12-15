#Constructor Variable and Static Variable

class Demo:

    ComName = "Google"

    def __init__(self):
        print("In Constructor")

    def empInfo(self):
        EmpAge = 21
        self.ComName = "Apple"
        print(self.ComName)
        print(Demo.ComName)

emp1 = Demo()

emp1.empInfo()

"""
O/p  In Constructor
     Apple
     Google
"""

