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
print(player[5])                                                                #Error : list index out of list

print(player[-1])                                                               #KlRahul
print(player[-3])                                                               #Virat

#2slicing

print(player[2: : ])                                                            #['Virat','Shreyas','KlRahul']
print(player[2:4:2])                                                            #['Virat']
print(player[ :5:3])                                                            #['Rohit','shreyas']

print(player[ : :3])                                                            #['Rohit','shreyas']
print(player[4:2:2])                                                            #[]
print(player[4:2:-1])                                                           #['klRahul','Shreyas']


















