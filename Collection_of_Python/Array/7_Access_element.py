'''
1. Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
'''

import array

my_array = array.array('i',[1,2,3,4,5,6])

for i in my_array:
    print(i, end = " ")

#Access individual element through indexes
print(my_array[0])
print(my_array[1])
print(my_array[2])
