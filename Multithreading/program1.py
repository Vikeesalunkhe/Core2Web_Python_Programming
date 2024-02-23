#/usr/lib/python3./threading.py

import threading

print("start code")
def fun():
    print("In fun function")

print(threading.current_thread().name)

fun()
