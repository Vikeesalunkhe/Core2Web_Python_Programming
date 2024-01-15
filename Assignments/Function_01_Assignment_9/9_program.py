'''
9. Write a real-time example of OOP on IPL cricket by the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method
'''

class IPL:

    TeamName = "CSK"

    def __init__(self):
        self.player = 12
        self.over = 20

    def TimeTable(self):
        print("add Time Table here")


Obj = IPL()
Obj.TimeTable()
