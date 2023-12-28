class Demo:

    def __init__(self):
        print("In Constructor 1")

    def __init__(self,x):
        print("In Constructor 2")

obj = Demo()

#O/p TypeError: Demo.__init__() missing 1 required positional argument: 'x'
