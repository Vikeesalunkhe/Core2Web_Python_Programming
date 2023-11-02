
#Nested Function

def outer():

    def inner():
        print("In inner function")

    inner()

    print("In outer")


print("start code")
outer()
print("end code")


"""
O/p

start code
In inner function
In outer
end code

"""

