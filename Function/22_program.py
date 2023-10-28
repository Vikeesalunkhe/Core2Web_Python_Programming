#Passing variable number og keyword argument to a function

def fun(**argv):
    print(type(argv))
    print(argv)


fun(x = 10, y = 20, z = 30)


"""
O/p <class 'dict'>
    {'x': 10, 'y': 20, 'z': 30}
"""
