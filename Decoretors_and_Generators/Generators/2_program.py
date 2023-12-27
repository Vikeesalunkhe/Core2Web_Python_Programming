def fun():
    print("Start fun")
    yield 10
    yield 20
    yield 30
    print("End fun")

ret = fun()
print(next(ret))


"""
O/p Start fun
    10
"""
