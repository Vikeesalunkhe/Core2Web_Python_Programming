Fileobj = open("Language_Data.txt", "r+")

print(Fileobj.tell())            #print cursor current possition
print(Fileobj.read(7))           #read only first 7 characters including \n 
print(Fileobj.tell())
print(Fileobj.read(10))
print(Fileobj.tell())
