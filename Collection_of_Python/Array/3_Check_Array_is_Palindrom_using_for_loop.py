import array

Data = array.array('i',[1,2,3,4,3,2,1])
ln = len(Data)
count = 0
for i in range(ln):

    if Data[i] == Data[ln - i - 1]:
        count+=1

if ln == count:
    print("array is palindorm")

else:
    print("array is not a palindrom")
