class Boss:
    pass

class Manager(Boss):
    pass

class TeamLead(Boss, Manager):
    pass

class Developer(TeamLead):
    pass

#TypeError: Cannot create a consistent method resolution order (MRO) for bases Boss, Manager

