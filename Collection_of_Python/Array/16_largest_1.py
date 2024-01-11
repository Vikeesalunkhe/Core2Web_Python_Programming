import array

arr = array.array('i',[3,2,1,5,6,8,3])
arr_list =  arr.tolist()
arr_list.sort()
print(arr_list)
ln = len(arr_list)
print("largest no. is : ",arr_list[ln-1])
