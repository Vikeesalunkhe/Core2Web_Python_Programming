from abc import ABC, abstractmethod

class College(ABC):

    def __init__(self):
        print("BE Engineering")

    @abstractmethod
    def Branch(self):
        pass

class Dhiraj(College):

    def Branch(self):
        print("Computer engineering")


class Vaibhav(College):

    def Branch(self):
        print("Robotics Engineering")

vaibhav = Vaibhav()
vaibhav.Branch()

dhiraj = Dhiraj()
dhiraj.Branch()



"""
BE Engineering
Robotics Engineering
BE Engineering
Computer engineering
"""
