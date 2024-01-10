import array

my_arr = array.array('i',[1,4,7,2,4])

print("current memory add., and lenght : ",my_arr.buffer_info())
print("the size of memory buffer in bytes : ",(my_arr.itemsize))
