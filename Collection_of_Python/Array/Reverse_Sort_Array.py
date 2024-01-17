import array

Data = array.array('i',[1,3,6,2,8,7,4,5])

ln = len(Data)
for i in range(ln):

    for j in range(ln-1):

        if Data[j] < Data[j+1]:
            x = Data.pop(j+1)
            Data.insert(j,x)

print(Data)
