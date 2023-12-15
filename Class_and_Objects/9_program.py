#Class Variable and Static Variable 

class Company:

    CompanyName = "Facebook"

    def __init__(self):
        print("In Constructor")
        self.empId = 12
        self.empName = "Kanha"

    def empInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.CompanyName)
        print(Company.CompanyName)
        print(company)

emp1 = Company()
emp2 = Company()

emp1.empInfo()
emp2.empInfo()

"""
O/p  In Constructor
     In Constructor
     12
     Kanha
     Facebook
     Facebook
     NameError: name 'company' is not defined. Did you mean: 'Company'?
"""

