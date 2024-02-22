fileobj = open("Student_data.txt", "r+")

copy_data = fileobj.readlines()
print(type(copy_data))
print(copy_data)


second_file = open("User_input.txt", "a")
second_file.writelines(copy_data)
