"""
4. Take a number from the user and check whether it is present in the list. If
it's in the list, print "Available."
List1 = [10, 20, 30, 40, 50]
#input: num = 10
#Output: available
#input num = 15
#Output:No Output
"""
def Cheak(num,listdata):

    for i in listData:
        if num == i:
            return "Available"

    return("not Avilable")

num = int(input("Enter value of num : "))
listData = [10,20,30,40,50,60]

ret = Cheak(num,listData)
print(ret)
