class Company:

    def disp(self):
        print("Hello")
        print(self)


obj = Company()
obj.disp()
print(obj)


"""
O/p  Hello
     <__main__.Company object at 0x7f5a3e52b6a0>
     <__main__.Company object at 0x7f5a3e52b6a0>

"""
