#print sum of two nu using def function


def sumTwo(a,b):
    print("In fun")
    sum_n = a+b
    print(sum_n)

x = int(input("Enter Value of x : "))    #10
y = int(input("Enyer value of y : "))    #20

sumTwo(x,y)
sumTwo(x+10, y+20)



#O/p  In fun
#     30
#     In fun
#     60
