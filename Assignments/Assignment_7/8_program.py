"""
8. Write a realtime example of oop which contains the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method
"""

class Project:

    Pro_Name = "Autonomous_Robot"                 #class variable
    def __init__(self):                           #constructor
        self.Total_Member = 4             
        self.GroupName = "sigma"                  #instance variable

    def cost(self):                               #instance methods
        self.Hardwer = 350
        self.sensor = 800
        print(self.Hardwer)
        print(self.GroupName)

obj = Project()
obj.cost()


