#passing variable number of keyword argument to a function

def fun(**argv,x,y):
    print(type(argv))
    print(argv)

fun(x = 10, p = 20, z = 30)



#O/p SyntaxError: invalid syntax


