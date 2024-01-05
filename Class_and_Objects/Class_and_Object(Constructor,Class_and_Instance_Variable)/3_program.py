class Data:

    def disp(self):
        print("Hello")
        print(type(self))

print("start code")
obj = Data()
obj.disp()
print("End code")
print(type(Data))


"""
O/p start code
    Hello
    <class '__main__.Data'>
    End code
    <class 'type'>
"""

