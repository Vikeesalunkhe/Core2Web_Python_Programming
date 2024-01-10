import array

my_arr = array.array('i',[1,2,3,4,5])

my_arr.extend(my_arr)
print(my_arr)
