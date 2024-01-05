class Employes:

    def __init__(self):
        print("In Constructor")
        self.x = 10
        self.y = 20

    def disp(self):
        print(self.x)
        print(self.y)

obj = Employes()
obj.disp()

"""O/p In Constructor
       10
       20
"""
