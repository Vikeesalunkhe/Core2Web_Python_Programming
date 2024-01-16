'''
4. Create one parent class with the attribute methods and instance variable,
write the same method in the child class, make the object of the child
class, call the method, and write the output.
'''

class parent:

    def __init__(self):
        print("parent constructor")
        self.name = "Virat"
        self.age = 21

    def attribut(self):
        print(self.name)
        print(self.age)

class Child(parent):

    def __init__(self):
        print("child constructor")
        self.name = "Mahi"
        self.age = 45

    def attribut(self):
        print(self.name)
        print(self.age)



Obj = Child()
Obj.attribut()


'''
O/p child constructor
    Mahi
    45
'''

