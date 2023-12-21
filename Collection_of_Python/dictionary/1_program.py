#dictionary
#1.mutable
#2.collection of different data tupe element in key:value format
#3.access element into key though
#4.A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#5.dict Write in curly brackets {}

dictData = {}

print(type(dictData))                                                     #<class 'dict'>

player1 = {45:"Rohit",77:"Shubman",18:"Virat",1:"KlRahul"}

print(type(player1))                                                       #<class 'dict'>

player2 = {45:"Rohit",77:"Shubman",18:"Virat",1:"KlRahul","next to bat":{96:"Shreyas",63:"Sky",8:"Jadu"}}

print(player2[18])                                                         #Virat
print(player2["next to bat"])                                              #{96: 'Shreyas', 63: 'Sky', 8: 'Jadu'}
print(player2["next to bat"][63])                                          #SKY
#print(player2[66])                                                         #KeyError 

player2[100] = "Virat Kohli"
print(player2)                                                             #{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'KlRahul', 'next to bat': {96: 'Shreyas', 63: 'Sky', 8: 'Jadu'}, 100: 'Virat Kohli'}


#################################################################
##methods in dict

##access
#1.get()
#2.items()
#3.keys()
#4.values()

player = {45:"Rohit",77:"Shubman",18:"Virat",1:"KlRahul"}

print(player.get(18))                                                       #Virat  :get the value of key

print(player.items())                                                       #dict_items([(45, 'Rohit'), (77, 'Shubman'), (18, 'Virat'), (1, 'KlRahul')])

for key,value in player.items():
    print(key,":",value)                                                    #45 : Rohit
                                                                            #77 : Shubman
                                                                            #18 : Virat
                                                                            #1 : KlRahul

print(player.keys())                                                        #dict_keys([45, 77, 18, 1])

print(player.values())                                                      #dict_values(['Rohit', 'Shubman', 'Virat', 'KlRahul'])

######
##delet
#1.pop()
#2.popitem()
#3.clear()

print(player.pop(18))                                                       #Virat
print(player)                                                               #{45: 'Rohit', 77: 'Shubman', 1: 'KlRahul'}

print(player.popitem())                                                     #(1, 'KlRahul')
print(player)                                                               #{45: 'Rohit', 77: 'Shubman'}

print(player.clear())                                                       #None
print(player)                                                               #{}

########
#1.copy()
#2.update()
#3.setdefault()
#4.fromkeys()

player = {45:"Rohit",77:"Shubman",18:"Virat",1:"KlRahul"}


playerData = player.copy()
print(playerData)                                                           #{45:"Rohit",77:"Shubman",18:"Virat",1:"KlRahul"}

lang = {"python":1991,"Cpp":1957,"java":1998}

playerData.update(lang)
print(playerData)                                                           #{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'KlRahul', 'python': 1991, 'Cpp': 1957, 'java': 1998}

player.setdefault(18,"Kohli")                                               #if present given key in dict. to not any changes in dict
print(player)                                                               #{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'KlRahul'}

player.setdefault(100,"Virat Kohli")                                        #if not present given key in dict to add given key:value in last of dict 
print(player)                                                               #{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'KlRahul', 100: 'Virat Kohli'}

lang = ["ReactJs","Flutter","Springboot"]
teacher = "shashi"

print(player.fromkeys(lang,teacher))                                        #{'ReactJs': 'shashi', 'Flutter': 'shashi', 'Springboot': 'shashi'}
print(player.fromkeys(lang))                                                #{'ReactJs': None, 'Flutter': None, 'Springboot': None}

print(player)                                                               #{45: 'Rohit', 77: 'Shubman', 18: 'Virat', 1: 'KlRahul', 100: 'Virat Kohli'}


















