'''
check largest no. element in array
'''

import array

arr = array.array('i',[11,4,2,66,8,2,3,9])
ln = len(arr)
i = 0
largest = 0

while (i<ln):

    if arr[i] > largest:
        largest = arr[i]
    i+=1

print(largest)
