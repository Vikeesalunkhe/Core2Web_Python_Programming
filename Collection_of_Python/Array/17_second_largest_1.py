import array

arr = array.array('i',[1,3,6,22,77,3,5,77,9])

arr_list = arr.tolist()
arr_list.sort()
print(arr_list)

ln = len(arr_list)
largest = arr_list[ln-1]
print("last First largest no. : ",largest)
second = -1
for i in range(ln-1,-1,-1):
    if arr_list[i] > second and largest != arr_list[i]:

        second = arr_list[i]
        break

print("last second largest no. : ",second)

