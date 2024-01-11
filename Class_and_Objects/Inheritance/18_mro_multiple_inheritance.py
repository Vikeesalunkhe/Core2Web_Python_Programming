class Boss:
    def fun(self):
        print("in fun:Boss")

class manager1(Boss):
    def fun(self):
        print("In fun:Maanager 1")

class manager2(Boss):
    def fun(self):
        print("In fun:Manager 2")

class TeamLead1(manager1,manager2):
    def fun(self):
        print("In fun:teamLead1")

class TeamLead2(manager2):
    def fun(self):
        print("In fun:teamLead2")

class Developer(TeamLead1,TeamLead2):
    pass

Developer()
print(Developer.__mro__)

#(<class '__main__.Developer'>, <class '__main__.TeamLead1'>, <class '__main__.manager1'>, <class '__main__.TeamLead2'>, <class '__main__.manager2'>, <class '__main__.Boss'>, <class 'object'>)

