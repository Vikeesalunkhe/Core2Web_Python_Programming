from program_2 import Data                    
#from 'program_file' import 'Class_name'

#from program_2 import *                                           #* : All 


class Parent(Data):

    def __init__(self):
        print("In parent constructor")

class Child(Parent):

    def __init__(self):
        print("In Child Constructor")



if __name__=='__main__':
    Child()
