#defult parameter

def add(x):
    print(x)

add(10,20)                #pass two arguments and define only 1 parameter does not support


#O/p TypeError: add() takes 1 positional argument but 2 were given



def add2(x,y):
    print(x,y)

add2(10,20,30)           #pass three argument and define only 2 param. does not support


#O/p TypeError: add2() takes 2 positional arguments but 3 were given
 

