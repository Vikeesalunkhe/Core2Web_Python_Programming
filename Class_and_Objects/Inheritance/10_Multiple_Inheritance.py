class Parent1:

    def __init__(self):
        print("In Const. Parent 1")

class Parent2:

    def __init__(self):
        print("In Const. Parent 2")

class Child(Parent1, Parent2):

    def __init__(self):
        print("In child Cons.")
        super().__init__()
        
    

obj = Child()


'''
O/p  In child Cons.
     In Const. Parent 1
'''

