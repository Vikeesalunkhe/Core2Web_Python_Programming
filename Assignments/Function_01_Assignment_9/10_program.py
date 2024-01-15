'''
10. Write a program in which you have to write a __new__ user-defined function that
creates a new instance of a class.
'''

class Demo:

    def __new__(self):
        print("In new ")



Demo()
