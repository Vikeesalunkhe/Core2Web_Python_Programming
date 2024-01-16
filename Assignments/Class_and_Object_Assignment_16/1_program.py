'''
1. Create a Class Human with instance attributes(including variables(name,
age) and methods(information)), create the object of the class pass the
name and age attributes to the object and access the variables in the
method information().
#Input:
name : Core2web
age : 7
'''

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def information(self):
        print(self.name)
        print(self.age)

name = input("Enter the name : ")
age = int(input("Enter value of age : "))

if __name__=="__main__":
    obj1 = Human(name, age)
    obj1.information()
