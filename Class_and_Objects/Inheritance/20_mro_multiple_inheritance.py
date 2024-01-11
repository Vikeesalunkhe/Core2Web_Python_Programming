class Boss:
    pass

class Manager1(Boss):
    pass

class Manager2(Boss):
    pass

class Manager3(Boss):
    pass

class TeamLead1(Manager2, Manager1):
    pass

class TeamLead2(Manager2,Manager3):
    pass

class Developer(TeamLead2, TeamLead1):
    pass

print(Developer.__mro__)


#(<class '__main__.Developer'>, <class '__main__.TeamLead2'>, <class '__main__.TeamLead1'>, <class '__main__.Manager2'>, <class '__main__.Manager3'>, <class '__main__.Manager1'>, <class '__main__.Boss'>, <class 'object'>)

