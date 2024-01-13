import array

arr = array.array('i',[10,2,3,11,4,5,6,30,20,7,7])

larg = arr[0]
for i in arr:

    if i > larg:

        larg= i

print("Largest Element in Array : ",larg)

ln = len(arr)
secondLarge = arr[0]

for i in arr:

    if (i > secondLarge) and (larg != i):
        secondLarge = i
'''
for i in range(ln-1,-1,-1):

    if arr[i] > se and larg != arr[i]:

        se = arr[i]
        
'''
print("Second Largest Element : ",secondLarge)

