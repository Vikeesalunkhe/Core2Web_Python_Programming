"""
3. Program 3: Write a Program to Find whether the number Is Even or Odd
Input: 4
Output: 4 is an Even Number!
"""

def EvenorOdd(x):

    def Even(x):
        
        if x % 2 == 0:
            print("{} is even number".format(x))
        
        return odd
        

    def odd(x):

        if x % 2  == 1:
            print("{} is odd number".format(x))

    return Even


num = int(input("Enter the value of num : "))

ret1 = EvenorOdd(num)
ret2 = ret1(num)
ret2(num)

print(ret1)
print(ret2)
print(type(ret1))
print(type(ret2))

