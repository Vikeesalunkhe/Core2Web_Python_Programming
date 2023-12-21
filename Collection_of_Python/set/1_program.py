#set()

setData = set()
print(setData)                                                   #set()
print(type(setData))                                             #<class 'set'>

setData = {1,2,3,4,5,6}
print(setData)                                                   #{1,2,3,4,5,6}

setData = {1,2,3,1,2,4,5,6} 
print(setData)                                                   #{1,2,3,4,5,6,}

setData = {1,2,3,10.4,True,False}
print(setData)                                                   #{1,2,3,10.4}

setData = {"Rahul","Ashish","Badhe","Kanha"}
print(setData)                                                   #{'Kanha','Badhe','Rahul','Ashish'}

setData = set([10,20,30,40])
print(setData)                                                   #{40,20,10,30}

#setData = set(10)
#print(setData)                                                   #TypeError : int varoable not itreable

setdata = set("Shashi")
print(setData)                                                   #{'s','h','a','s','h','i'}

############
setData = {1,2,3,4,5,6}
#print(setdata[3])                                                #TypeError : set is not subscript (index no, not support)

#######
#Metods in set
#1.add()
#2.copy()
#3.difference()
#4.difference_update()
#5.discard()
#6.intersetion()
#7.intersection_update()
#8.isdisjoint()
#9.issubset()
#10.issuperset()
#11.symmetric_difference()
#12.symmetric_difference_update()
#13.union()
#14.update()
#15.pop()
#16.remove()
#17.clear()

#1.add()       : add data

setData1 = {1,2,3,4}

setData1.add(10)
print(setData1)                                                  #{1,2,3,4,10}


#2.copy()         : copy all element in copid set
setdata1 = {1,2,3,4}  

setdata2 = setdata1.copy()
print(setdata2)                                                 #{1,2,3,4}

#3.difference()  

setdata1 = {1,2,3,4}
setdata2 = {3,4,5,6}

setData3 = setdata1.difference(setdata2)
print(setData3)                                                 #{1,2}

#4.difference_update

setData1 = {1,2,3,4}
setData2 = {3,4,5,6}

setData1.difference_update(setData2)
print(setData1)                                                 #{1,2}

#5.discard()

setData1 = {1,2,3,4}
setData1.discard(3)                  
print(setData1)                                                 #{1,2,4}
                                                                    
#6.intersection()

setData1 = {1,2,3,4}
setData2 = {3,4,5,6}

#setData3 = setData1.intersection(SetData2)
print(setData3)

#7.intersection_update()

setData1.intersection_update(setData2)
print(setData1)                                               #{3,4}

#8.isdisjoint()

setData1 = {1,2,3,4}
setData2 = {3,4,5,6}

print(setData1.isdisjoint(setData2))                          #False

#9.issubset()

setData1 = {1,2,3,4}
setData2 = {3,4,5,6}
setData3 = {3,4,5,1,2,6}
print(setData1.issubset(setData2))                            #False
print(setData1.issubset(setData3))                            #True

#10.issuperset()

setData1 = {1,2,3,4}
setData2 = {3,4,5,6}
setData3 = {1,3,4,2}
print(setData1.issuperset(setData2))                         #False
print(setData1.issuperset(setData))                          #false

#11.symmetric_difference()

setData3 = setData1.symmetric_difference(setData2)
print(setData3)                                             #{1,2,5,6}

#12.symmetric_difference_update()

setData1.symmetric_difference_update(setData2)
print(setData1)                                             #{1,2,5,6}

#13.union()

setData1 = {1,2,3,4}
setData2 = {3,4,5,6}

setData3 = setData1.union(setData2)
print(setData3)                                             #{1,2,3,4,5,6}

#14.update()

setData1.update(setData2)
print(setData1)                                             #{1,2,3,4,5,6}

#15.pop()

setData1 = {1,2,3,4,5,6}

setData1.pop()
print(setData1)                                             #{2,3,4,5,6}

#16.remove()

setData1 = {10,20,30,40}

setData1.remove(20)
print(setData1)                                             #{40,10,30}

#17.clear()

setData1 = {1,4,7,8.7,3,"a"}
setData1.clear()
print(setData1)                                             #set()

















