#Function Decoretors

def Demo(func):


    def inner():
        data = [1,2,3,4,5]
        for i in data:
            print(i)
            func()
    return inner

@Demo
def normalFun():
    print("Hello, in normal function")

normalFun()

"""
O/p
1
Hello, in normal function
2
Hello, in normal function
3
Hello, in normal function
4
Hello, in normal function
5
Hello, in normal function
"""
