#8. Draw the flow diagram for the following code.

class Demo:

    def __init__(self):
        print("In Constructor")

    def __del__(self):
        print("in destructor")

def Fun():
    print("In fun")
    obj = Demo()
    print("End fun")
    return obj

retObj = Fun()
print("End code")


"""
O/p In fun
In Constructor
End fun
End code
in destructor
'''
