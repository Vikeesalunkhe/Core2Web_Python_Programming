fileobj = open("User_input.txt", "a")

while True:
    data = input("Enter data : ")
    if data == "stop":
        break

    fileobj.writelines(data)


#print(fileobj.read())
