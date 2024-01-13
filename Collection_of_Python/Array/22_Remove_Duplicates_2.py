import array

arr = array.array('i',[1,1,2,2,2,4,5,6,6])
ln = len(arr)

i = 0
for j in range(ln):                #ln = 9

    if arr[i] != arr[j]:
        arr.insert(i+1,j)
        i+=1
    

print(arr)


