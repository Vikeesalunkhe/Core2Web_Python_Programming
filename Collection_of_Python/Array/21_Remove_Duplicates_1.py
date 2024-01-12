import array

arr = array.array('i',[1,1,2,3,3,3,4,5,5,6])

my_set = set()
for i in arr:
    my_set.add(i)

print(my_set)
