#class variable and static variable

class Company:

    ComName = "Facebook"                                #class variable

    def __init__(self):
        print("In Cunstructor")
        self.empId = 12
        self.empName = "Kanha"

    def empInfo(self):
        totalemp = 10
        print(totalemp)
        print(self.empId)
        print(self.empName)                            
        print(self.ComName)                           #instance name space variable
        print(Company.ComName)                        #class name space variable


emp1 = Company()
emp1.empInfo()
print(Company.ComName)


"""
O/p  In Cunstructor
     10
     12
     Kanha
     Facebook
     Facebook
     Facebook

"""
