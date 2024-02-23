import threading

def fun(x,y):
    print("In fun function")
    print(x)
    print(y)

print(threading.current_thread().name)

thread = threading.Thread(target = fun, args = [10,20])
thread.start()
