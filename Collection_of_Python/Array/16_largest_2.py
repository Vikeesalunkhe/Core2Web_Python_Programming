import array

arr = array.array('i',[2,4,7,9,1,2,5,1,])

largest = 0

for i in arr:

    if i > largest:
        largest = i

print(largest)
