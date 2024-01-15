def outer():
    def inner():
        return "Gretings from the inner function"

    return inner()

if __name__=="__main__":
    result = outer()
    print(result)


#O/p gretiting from the inner function
