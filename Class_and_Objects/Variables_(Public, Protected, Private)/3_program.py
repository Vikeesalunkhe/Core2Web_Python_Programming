class Demo:

    def __init__(self):
        print("In Constructor")
        self.x = 10
        self._y = 20
        self.__z = 30

    def __fun(self):
        print("In Private fun")

obj = Demo()
obj._Demo__fun()


