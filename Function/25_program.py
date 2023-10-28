#passing variable number of keyword argument to a function

def fun(**argv):
    for key,value in argv.items():
        print(key, ":", value)


fun(x = 10, y = 20, z = 30)

"""
O/p  x : 10
     y : 20
     z : 30
"""

