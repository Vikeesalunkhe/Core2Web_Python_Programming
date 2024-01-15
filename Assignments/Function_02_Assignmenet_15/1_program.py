def add(x):
    def inner(y):
        return x*y

    return inner

if __name__=="__main__":
    add3 = add(3)
    result = add3(7)
    print(result)



#O/p 21
