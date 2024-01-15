'''
3. WAP for function returns the array of factorial of the element
● Pass the array to the function
Input: [1, 2, 3, 4, 5]
Output:[1, 2, 6, 24, 120]
'''

import array as arr

def Factorial(num):

    for i in num:
        fact = 1
        for j in range(1,i+1):
            fact = fact*j
        New.append(fact)




Normal = arr.array('i',[1,2,3,4,5])
New = arr .array('i',[])

Factorial(Normal)
print(New)


