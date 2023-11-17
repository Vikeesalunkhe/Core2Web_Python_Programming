#1.Multiple Object Store
#2.Store Different Datatype object
#3.Mutable
#4.indexing
#5.Growable

#list literals

batman = ["Rohit","Shubman","Virat","KLRahul"]
print(batman)                                                                     #['Rohit', 'Shubman', 'Virat', 'KLRahul']
print(type(batman))                                                               #<class 'list'>

batrun = ["rohit",45,"Shubman",80,"Virat",117,7.7]
print(batrun)                                                                      #["rohit",45,"Shubman",80,"Virat",117,7.7]
print(type(batrun))                                                                #<class 'list'>

employee = [{10,"Ashish",1.5},{11,"Kanha",77.5}]
print(employee)                                                                    #employee = [{10,"Ashish",1.5},{11,"Kanha",77.5}]
print(type(employee))                                                              #<class 'list'>

########################################################
#List Constructor

player = list()
print(player)                                                                     #[]
print(type(player))                                                               #<class 'list'>

listData = [10,20,30,40]

batsman = list(listData)
print(batsman)                                                                   #[10,20,30,40]
print(type(batsman))                                                             #<class 'lisit'>

setData = {"vikee",10,3.3,30,40}

Run = list(setData)
print(Run)                                                                      #[30,40,'vikee',3.3,10]
print(type(Run))                                                                #<class 'list'>

tupleData = (10,20,30,40)

Score = list(tupleData)
print(Score)                                                                   #[10,20,30,40]
print(type(Score))                                                             #<class 'list'>

dictData = {"Virat":18,"Rohit":45,"Mahi":7}

jrNo = list(dictData)
print(jrNo)
print(type(jrNo))

###########################################################
#list Comprehension


normlist = [num for num in range(1,11)]

print(normlist)                                                                 #[1,2,3,4,5,6,7,8,9,10]
print(type(normlist))                                                           #<class 'list'>

even_list = [num for num in range(1,11) if num % 2 == 0]

print(even_list)                                                                #[2,4,6,8,10]
print(type(even_list))                                                          #<class 'list'>

odd_list = [i for i in range(1,11) if i % 2 == 1]

print(odd_list)                                                                 #[1,3,5,7,9]
print(type(odd_list))                                                           #<class 'list'>


##############################################################
#accessing element from list
#1.index
#2.slicing


player = ["Rohit","Shubman","Virat","Shreyas","KlRahul"]

print(player[0])                                                                #Rohit
print(player[2])                                                                #Virat
print(player[4])                                                                #KlRahul
#print(player[5])                                                                #Error : list index out of list

print(player[-1])                                                               #KlRahul
print(player[-3])                                                               #Virat

#2slicing

print(player[2: : ])                                                            #['Virat','Shreyas','KlRahul']
print(player[2:4:2])                                                            #['Virat']
print(player[ :5:3])                                                            #['Rohit','shreyas']

print(player[ : :3])                                                            #['Rohit','shreyas']
print(player[4:2:2])                                                            #[]
print(player[4:2:-1])                                                           #['klRahul','Shreyas']

print(player[-1:-5: ])                                                          #[]
print(player[-2:-4:-2])                                                         #['Shreyas']
print(player[-1: : -1])                                                         #['KlRahul','Shreyas','Virat','Shubman','Rohit']


##################################################################
#Methods from list
##access
#1.append
#2.extend
#3.insert

player = ["Rohit","Shubman","Virat","Shreyas","KlRahul"]

player.append("SKY")                                                           #.append : add single element in last index of list
print(player)                                                                  #['Rohit','Shubman','Virat','Shreyas','KlRahul','SKY']

player.extend(["Jagu","Mahi"])                                                 #.extend : add multiple data in last indexcess
print(player)                                                                  #['Rohit','Shubman','Virat','Shreyas','KlRahul','SKY','jagu','Mahi']

player.insert(3,"Hardik")                                                       #.index : replace single element in given index no.
print(player)                                                                  #['Rohit','Shubman','Virat','Hardik','KlRahul','SKY','jagu','Mahi']

#########

##Delet
#1.remove
#2.pop
#3.clear

player.remove("SKY")                                                        #.remove : remove or delet given element
print(player)                                                               #['Rohit', 'Shubman', 'Virat', 'Hardik', 'Shreyas', 'KlRahul', 'Jagu', 'Mahi']

player.pop()                                                                #.pop : remeove or delet last index element in list
print(player)                                                               #['Rohit', 'Shubman', 'Virat', 'Hardik', 'Shreyas', 'KlRahul', 'Jagu']

player.clear()                                                              #.clear : clear all list or empty list
print(player)                                                               #[]

########

#1.count()
#2.index()
#3.reverse()
#4.sort
#5.copy

player1 = ["Rohit","Shubman","Virat","Shreyas","KlRahul"]

newList = player1.copy()                                                    #copy the same list as player1 to newList
print(newList)                                                              #['Rohit', 'Shubman', 'Virat', 'Shreyas', 'KlRahul']
print(player1)                                                               #['Rohit', 'Shubman', 'Virat', 'Shreyas', 'KlRahul']

print(player1.index("Virat"))                                                #2  : gives index no. of element

print(player1.reverse())                                                     

print(player1.sort())                                                        #sort alphabetically

print(player1.count("Virat"))                                                #1  : count total no. of given element 













