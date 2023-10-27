
#return in Multiple value in def function

def add(x,y,z):
    x = x + 10
    y = y + 10
    z = z + 10
    return x,y,z

num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))
num3 = int(input("Enter value of num3 : "))

#ret_value = add(num1,num2,num3)
a,b,c = add(num1,num2,num3)
print(a)
print(b)
print(c)



"""
O/p 20
    30
    40
"""
