#from threading import Thread
import threading

def fun():
    print("In fun function")
    print(threading.current_thread().name)

    for i in range(5):
        print("In fun")

def gun():
    print("In gun function")
    print(threading.current_thread().name)

    for x in range(5):
        print("In gun")

print(threading.current_thread().name)

thread1 = threading.Thread(target = fun)
thread2 = threading.Thread(target = gun)

thread1.start()
thread2.start()


