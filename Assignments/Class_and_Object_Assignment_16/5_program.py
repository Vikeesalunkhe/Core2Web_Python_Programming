#5. Write a real-time example of Cricket that describes the inheritance

class ICC:

    def __init__(self):
        self.Teamname = "India"

    def Teamdata(self):
        print(self.Teamname)


class BCCI:

    def __init__(self):
        self.Teamname = "MaharashtraState"

    def TeamInfo(self):
        print(self.Teamname)


class IPL(ICC, BCCI):

    def __init__(self):
        self.Teamname = ["Mumbai", "CSK", "Channai"]

    pass

Obj = IPL()

Obj.Teamdata()
Obj.TeamInfo()


'''
['Mumbai', 'CSK', 'Channai']
['Mumbai', 'CSK', 'Channai']
'''
