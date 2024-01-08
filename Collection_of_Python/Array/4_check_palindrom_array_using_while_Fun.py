import array

def Palindrom(num):

    ln = len(num)
    count = 0
    i=0

    while i<ln:
        if num[i] == num[ln - i - 1]:
            count +=1
        
        i+=1
    if ln == count:
        return "array is Palindrom"

    else:
        return "array is not a Palindrom"

Data = array.array('i',[1,2,3,4,3,2,1])
print(Palindrom(Data))

'''

def Palindrom(num):

    ln = len(num)
    palindrom = 0
    i = 0
    while i<ln:                       #or while(i<ln//2)

        if num[i] != num[ln-i-1]:
            palindrom = 1
            break
        i+=1

    if palindrom == 1:
        return "Array is not a Palindrom"

    else:
        return "array is palindrom"

Data2 = array.array('i',[11,22,33,44,44,33,22,11])
print(Palindrom(Data2))
'''

