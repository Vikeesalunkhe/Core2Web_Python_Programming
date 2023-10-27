#addition of given no.  eg. 5 (1+2+3+4+5+=15)

def addition(x):
    sum = 0
    for i in range(x+1):
        sum = sum + i

    print(sum)

num = int(input("Enter value of num : "))
addition(num)
    
