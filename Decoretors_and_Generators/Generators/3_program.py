def fun():

    print("Start fun")
    yield 10+10
    yield 20+20
    yield 30+30
    print("End fun")
    



ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))


"""
O/p Start fun
    20
    40
    60
"""
