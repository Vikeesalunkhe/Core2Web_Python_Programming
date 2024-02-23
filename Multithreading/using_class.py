import threading
#from threading import Thread

class Mythread(threading.Thread):

    def run(self):
        print("In run fun")
        print(threading.current_thread().name)

print(threading.current_thread().name)

obj = Mythread()
obj.start()
