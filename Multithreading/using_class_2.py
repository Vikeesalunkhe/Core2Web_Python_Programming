import threading

class MyTread(threading.Thread):

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def display(self):
        print(self.x)
        print(self.y)
        print(threading.current_thread().name)

print(threading.current_thread().name)
obj = MyTread(20, 30)
t1 = threading.Thread(target = obj.display)
t1.start()
