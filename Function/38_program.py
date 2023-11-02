#Function return in function

def outer():

    def inner1(x,y):
        print("Inner1")

    return inner1
    print("In outer")


retObj = outer()
retObj(10,20)



#O/p Inner1

