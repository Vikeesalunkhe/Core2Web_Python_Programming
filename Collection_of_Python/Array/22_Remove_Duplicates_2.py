import array

arr = array.array('i',[1,1,2,2,2,4,5,6,6])
new = array.array('i',[])
ln = len(arr)
num = -1
for i in range(ln):
    
    if num < arr[i] and num != arr[i]:
        num = arr[i]
        new.append(arr[i])


print(new)

