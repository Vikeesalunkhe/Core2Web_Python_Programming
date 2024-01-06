class Manager:

    def project(self):
        print("In project:manager")

class TeamLead1:

    pass

class TeamLead2:

    def project(self):
        print("In project:Teamlead")


class Developer(TeamLead1, TeamLead2):
    pass

obj = Developer()
obj.project()


# O/p In project:Teamlead

