#constructor and instance variable

class Employee:

    CompanyName = "Facebook"
    
    def __init__(self):
        print("In Constructor")
        self.empId = 12
        self.empName = "Kanha"

    def empInfo(self):
        print(self.empId)
        print(self.empName)

emp1 = Employee()
emp2 = Employee()

emp1.empInfo()
emp2.empInfo()



""""
O/p In Constructor
    In Constructor
    12
    Kanha
    12
    Kanha
"""

