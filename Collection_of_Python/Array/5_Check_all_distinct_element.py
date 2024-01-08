
import array 

my_arr = array.array('i',[1,1,2,3,4,5,6,7])
setdata = set()

for i in my_arr:
    setdata.add(i)


if len(setdata) == len(my_arr):
    print("all distinct element")

else:
    print("not all distinct element")
