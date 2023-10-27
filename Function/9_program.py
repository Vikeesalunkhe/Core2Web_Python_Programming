#return Multiple value in from function


def addByTen(x,y,z):
    x = x + 10
    y = y + 10
    z = z + 10
    return x,y,z


val1 = int(input("Enter value of num1 : "))
val2 = int(input("Enter value of num2 : "))
val3 = int(input("Enter value of num3 : "))

ret = addByTen(val1,val2,val3)

print(type(ret))                                #<class 'tuple'>
print(ret)                                      #(20,30,40)




"""
O/p <class 'tuple'>
    (20, 30, 40)

"""
