#output in python

#formatted output

x = 10
y = 20.5
a = "vikee"


print("value of x = %d" %x)           #value of x = 10
print("value of y = %f" %y)           #value of y = 20.5
print("I am %s" %a)                   #I am vikee


print("x = %d" %x)                     #%10
print('y = %f' %y)                     #%20.5
print("a = %s" %a)                     #%vikee


print("Value of x = {}".format(x))                                      #value of x = 10
print('Value of y = {}'.format(y))                                      #Value of y = 20.5
print("my name is {} and my age is {}".format(a,y))                     #my name is vikee and age is 20.5
print("""value of x is {} and value of y is {}""".format(x,y))          #value of x is 10 and value of y is 20.5
