'''
Write a program print reverse array
'''

import array 

my_array = array.array('i',[1,2,3,4,5,6])
print("Original array : ",(my_array))
my_array.reverse()
print(my_array)
