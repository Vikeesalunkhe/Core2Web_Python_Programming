"""
9. Write a real-time example of OOP on IPL cricket by the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method
"""

class TimeTable:

    Location = "Mumbai"
    def __init__(self):
        self.TeamName = "CSK"
        self.Date = "22 March 24"

    def PlayerInfo(self):
        totalPlayer = 15
        print(self.TeamName)
        print(self.Date)
        print(totalPlayer)

obj = TimeTable()
obj.PlayerInfo()
