import array

my_array = array.array('i',[1,2,3,4,5,6,7])
ln = len(my_array)
i = 0
setData = set()

while i<ln:

    setData.add(my_array[i])
    i+=1

if len(setData) == len(my_array):
    print("all element distinct")

else:
    print("not all element distinct")


