from abc import ABC

class Demo(ABC):

    def __init__(self):
        print("In constructor")

    @abstractmethod
    def AbstractMethod(self):
        print("In Abstract Method")




