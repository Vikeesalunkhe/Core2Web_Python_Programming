import array

arr = array.array('i',[1,1,2,2,2,3,4,6,6,7,9,10])
new = array.array('i',[arr[0]])
ln = len(arr)
i = 0

for j in range(ln):
    if arr[i] != arr[j]:
        arr[i+1] = arr[j]
        new.append(arr[j])
        i+=1


print(new)

    
