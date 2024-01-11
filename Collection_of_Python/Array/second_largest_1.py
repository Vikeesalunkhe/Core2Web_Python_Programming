import array

arr = array.array('i',[1,5,88,2,7,33,88,3])
largest = 0
ln = len(arr)

for i in range(ln):
    if arr[i] > largest:
        largest = arr[i]

print(largest)


second_larg = -1

for i in arr:

    if i > second_larg and largest > i:
        second_larg = i




print(second_larg)


