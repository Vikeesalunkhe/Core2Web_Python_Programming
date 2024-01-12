import array

arr = array.array('i',[1,2,3,3,4,5,6])
ln = len(arr)


for i in range(1,ln):
    if arr[i-1] <= arr[i]:
        pass

    else:
        print("False")





