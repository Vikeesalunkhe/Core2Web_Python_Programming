Fileobj = open("Language_Data.txt", "r+")

print(Fileobj.read())

Fileobj.seek(10)
print(Fileobj.read())


"""File_Data
Java
Cpp
Python
Dart
BackEnd
FrontEnd

''''O/p
ython
Dart
BackEnd
FrontEnd
"""

