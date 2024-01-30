list1 = ['H', 'E', 'L', 'L', 'O']

ln = len(list1)
num = 0
for i in range(ln-1):

    x = list1.pop(num)
    list1.insert(ln-1-i, x)
    

print(list1)
