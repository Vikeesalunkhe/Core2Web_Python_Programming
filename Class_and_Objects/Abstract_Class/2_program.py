from abc import ABC, abstractmethod

class Hyundai():

    def __init__(self):
        print("In constuctor")


    @abstractmethod
    def carType(self):
        pass


class Creata(Hyundai):

    def carType(self):
        print("Sedan")

class Verna(Hyundai):

    def carType(self):
        print("SUV")


obj1 = Creata()
obj1.carType()

obj2 = Verna()
obj2.carType()



"""
In constuctor
Sedan
In constuctor
SUV
"""
