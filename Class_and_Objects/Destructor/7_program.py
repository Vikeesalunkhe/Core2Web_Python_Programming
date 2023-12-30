class Demo:

    def __init__(self):
        print("In Constructor")

    def __del__(self):
        print("In Destructor")

def Fun():
    print("In Fun")
    obj = Demo()
    print("End Fun")


Fun()
print("End Code")


"""
O/p In Fun
    In Constructor
    End Fun
    In Destructor
    End Code
"""
