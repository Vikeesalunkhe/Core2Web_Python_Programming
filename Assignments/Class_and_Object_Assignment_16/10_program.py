#10. Write the real-time example of Inheritance.

class Father:

    def __init__(self):
        print("In father constuctor")

class Mother:

    def __init__(self):
        print("In Mother constructor")


class child(Father, Mother):
    pass


Obj = child()



#O/p in Father constuctor
