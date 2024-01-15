def outer():
    message = "I am the outer functionn"

    def inner():
        return message

    return inner

if __name__=="__main__":
    inner_function = outer()
    result = inner_function()
    print(result)



#O/p I am the outer function
