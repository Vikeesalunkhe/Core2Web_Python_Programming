#passing multiple variables numbers of arguments in to function

def fun(*argv,x,y):
    print(x)
    print(y)
    print(argv)


fun(10,20)


#O/p TypeError: fun() missing 2 required keyword-only arguments: 'x' and 'y'

