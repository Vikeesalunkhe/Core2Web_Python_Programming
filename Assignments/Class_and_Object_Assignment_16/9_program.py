'''
9. Write a real-time example for classes and objects which include
@classmethod, @staticmethod, and instance method.
'''

class College:

    mark = 100

    def __init__(self, name):
        self.classname = name
        self.classNo = 12

    def Classdata(self):
        print("in class Data")
        print(self.classNo)
        print(self.classname)

    @classmethod
    def StudentMark(cls):
        print("In student mark")
        print(cls.mark)

    @staticmethod
    def studentInfo():
        password = 123 
        print("In student info")
        print(password)


Obj = College("IIT")

Obj.Classdata()
#College.Classdata(Obj)

Obj.StudentMark()
#College.StudentMark()

Obj.studentInfo()
#College.studentInfo()


'''
O/p in class Data
    12
    IIT
    In student mark
    100
    In student info
    123
'''


