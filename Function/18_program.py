#Passing variable of argument to a function

#varaggs

def fun(*argv):
    print(argv)
    print(type(argv))

fun(10,20,30)


#O/p (10, 20, 30)
#    <class 'tuple'>

