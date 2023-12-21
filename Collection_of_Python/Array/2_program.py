import array as arr
#import array
#from import array *


listData  = [100,200,300]
data = arr.array('i',[10,20,30,40,50])

#1.append()   : add given object in last of array
data.append(60)         
print(data)                         #array('i',[10,20,30,40,50,60])


#2.buffer_info()   : print Addresess of array and total no og element
print(data.buffer_info())           #(139660834797680, 6)


#3.count()   : count is find which times present given Obj. in array
print(data.count(30))               #1


#4.extend()   :Add multiple Obj. in array (two or more)
data.extend([70,80])
print(data)                         #array('i', [10, 20, 30, 40, 50, 60, 70, 80])


#5.fromlist()  : add all list elemnt in array 
data.fromlist(listData)
print(data)                         #array('i', [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 300])


#6.index()  : find index no. of given Obj.
print(data.index(40))               #3


#7.insert()  : insert Obj. in perticular index no.
data.insert(4,500)
print(data)                         #array('i', [10, 20, 30, 40, 500, 50, 60, 70, 80, 100, 200, 300])


#8.pop()  : delete last index element in array
print(data.pop())                   #300
print(data)                         #array('i', [10, 20, 30, 40, 500, 50, 60, 70, 80, 100, 200])


#9.remove()  : remove given Obj. in array
data.remove(500)
print(data)                         #array('i', [10, 20, 30, 40, 50, 60, 70, 80, 100, 200])


#10.reverse()  : reverse is change the reverse sequance of array
data.reverse()
print(data)


#11.tolist()  : convert array to list
print(data.tolist())                 #[200, 100, 80, 70, 60, 50, 40, 30, 20, 10]




