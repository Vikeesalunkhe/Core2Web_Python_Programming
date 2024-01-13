'''
8. Write a realtime example of oop which contains the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method
'''

class Student:

    Name = "vikee"

    def __init__(self):
        self.ID = 23
        self.Age = 21

    def Data(self):
        print("ID : ",self.ID)
        print("Age : ",self.Age)


obj = Student()
obj.Data()


