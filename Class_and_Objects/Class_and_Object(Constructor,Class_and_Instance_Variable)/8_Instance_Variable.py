#Constructor and instance variable

class Employee:

    def __init__(self,empId,empName):
        print("In Constructor")
        self.empId = empId
        self.empName = empName

    def empInfo(self):
        print(self.empId)
        print(self.empName)

emp1 = Employee(12,"Kanha")
emp2 = Employee(15,"Ashish")

emp1.empInfo()
emp2.empInfo()


"""
O/p  In Constructor
     In Constructor
     12
     Kanha
     15
     Ashish
"""

