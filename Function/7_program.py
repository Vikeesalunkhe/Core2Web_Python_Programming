#return statement in function

#print factor of given user input using def fun

def factor(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i

    return fact

num = int(input("Enter Vlaue of num : "))
ret = factor(num)
print(ret)

