Fileobj = open("Student_data.txt", "r+")

Fileobj.seek(10)
print(Fileobj.read())


"""
File_Data 
    Vishal
    vikee
    vaibhav
    lalit
    vinay
    vaibhav
    lalit
    vinay

"""
"""
O/p ee
    vaibhav
    lalit
    vinay
    vaibhav
    lalit
    vinay
"""

