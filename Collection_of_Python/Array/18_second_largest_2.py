import array 

arr = array.array('i',[1,5,2,55,22,44,9,1,44,0])
larg = 0

for i in arr:
    if i > larg:
        larg = i

print("This is last First largest no. : ",larg)
second_larg = -1

for i in arr:
    if i > second_larg and larg != i:
        second_larg = i

print("This is second Largest no. : ",second_larg)
