class Demo:
    def __init__(self):
        print("In Constructor")

    def __del__(self):
        print("In Destructor")


def Fun():
    print("In Fun")
    obj = Demo()
    print("End Fun")
    return obj


retobj = Fun()
print("End Code")
