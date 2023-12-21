def gun():
    print("In gun")

def run(y):
    print("In run")
    y()

def fun(x):
    print("In fun")
    x()

fun(run(gun))


"""
O/p In run
    In gun
    In fun
    TypeError: 'NoneType' object is not callable
"""
