from abc import ABC, abstractmethod

class Main(ABC):

    def __init__(self):
        print("In constructor")

    @abstractmethod
    def AbstractMethod(self):
        print("In Abstract Method")

class SubMain1(Main):

    def AbstractMethod(self):
        print("Sub main 1")

class SubMain2(Main):

    def AbstractMethod(self):
        print("Sub main 2")


obj1 = SubMain1()
obj1.AbstractMethod()

obj2 = SubMain2()
obj2.AbstractMethod()


"""
In constructor
Sub main 1
In constructor
Sub main 2
"""

