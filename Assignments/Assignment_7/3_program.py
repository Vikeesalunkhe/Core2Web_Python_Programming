"""
3. WAP for function returns the array of factorial of the element
"""
import array as arr

def Factorial(my_array):

    for i in my_array:
        num = 1
        for j in range(1,i+1):
            num = num*j
        print(num)
            

my_array = arr.array('i',[1,2,3,4,5,6,7,8,9,10])
Factorial(my_array)


"""
O/p 1
    2
    6
    24
    120
    720
    5040
    40320
    362880
    3628800
"""

