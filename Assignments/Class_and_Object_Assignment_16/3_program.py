'''
3.Create the Parent have the @classmethod, @staticmethod, and instance
method, and call all these functions by creating the object of a child class.
'''

class Parent:

    def Instance(self):
        print("In Instance method")

    @classmethod
    def ClassMethod(cls):
        print("In class method")

    @staticmethod
    def StaticMethod():
        print("In Static Method")

class Child(Parent):
    pass

Obj = Child()
Obj.ClassMethod()
Obj.StaticMethod()
Obj.Instance()
Child.Instance(Obj)


'''
O/p In class method
    In Static Method
    In Instance method
    In Instance method
'''



