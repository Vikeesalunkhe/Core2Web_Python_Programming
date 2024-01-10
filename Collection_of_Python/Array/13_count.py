'''
6. Write a Python program to get the number of occurrences of a specified element in an array.
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
Number of occurrences of the number 3 in the said array: 3
'''
import array 

my_array = array.array('i',[1,5,2,3,8,3,6,3])
print("Number of occurrences of the number 3 in the said array : ",my_array.count(3))
