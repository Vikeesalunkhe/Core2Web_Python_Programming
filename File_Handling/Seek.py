fileobj = open("Student_data.txt", "r")

fileobj.seek(10)                       #seek : skip first 10 characters
print(fileobj.read())

