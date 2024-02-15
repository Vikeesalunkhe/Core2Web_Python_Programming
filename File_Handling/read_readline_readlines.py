
Fileobj = open("Language_Data.txt", "r+")

print(Fileobj.read(3))                #print only first 3 characters includeing \n

print(Fileobj.readline())              #print first line only (upto first \n)
print(Fileobj.readline(3))             #print first 3 char in first line

print(Fileobj.readlines())              #print all line inside the square bracket[]
print(Fileobj.readlines(1))              #['Java\n']
print(Fileobj.readlines(12))             #['Java\n', 'Cpp\n', 'Python\n']



