class Parent:
    def __init__(self):
        print("Parent Constructor 1")

    def __init__(self):
        print("Parent Constructor 2")

obj = Parent()


#O/p AttributeError: 'Demo' object has no attribute 'z'

