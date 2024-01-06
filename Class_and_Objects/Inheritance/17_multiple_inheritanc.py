class Boss:
    def report(self):
        print("Boss:report")


class Manager1:
    def report(self):
        print("Manager1:report")


class Manager2:
    def report(self):
        print("Manager2:report")


class Manager3:
    def report(self):
        print("Manager3:report")


class TeamLead1(Manager1, Manager3):
    def report(self):
        print("TeamLead1:report")


class TeamLead2(Manager2, Manager3):
    def report(self):
        print("TeamLead2:report")

class Developer(TeamLead1, TeamLead2):

    def report(self):
        print("Developer:report")


obj = Developer()
print(Developer.mro())
#print(Developer.__mro__)


'''
O/p [<class '__main__.Developer'>, <class '__main__.TeamLead1'>, <class '__main__.Manager1'>, <class '__main__.TeamLead2'>, <class '__main__.Manager2'>, <class '__main__.Manager3'>, <class 'object'>]
'''
