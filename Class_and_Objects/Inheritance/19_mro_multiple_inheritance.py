class Boss:
    def report(self):
        print("In repo:Boss")

class Manager1(Boss):
    def report(self):
        print("In repo:Manager1")

class Manager2(Boss):
    def report(self):
        print("In repo:Manager2")

class TeamLead1(Manager1,Manager2):
    def report(self):
        print("In repo:TeamLead1")

class TeamLead2(Manager2,Manager1):
    def report(self):
        print("In repo:TeamLead2")

class Developer(TeamLead1, TeamLead2):
    pass

print(Developer.__mro__)



#O/p TypeError: Cannot create a consistent method resolution order (MRO) for bases Manager1, Manager2
