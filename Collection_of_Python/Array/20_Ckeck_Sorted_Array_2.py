import array

def Sorted(ln,arr):

    i = 1
    while (i<ln):
        if arr[i] >= arr[i-1]:
            pass

        else:
            return False
        i+=1
    return True

arr = array.array('i',[1,3,3,4,6,7,8])
ln = len(arr)
print(Sorted(ln,arr))

