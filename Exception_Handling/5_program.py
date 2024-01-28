#Exeption Handling


list1 = [10, 'kanha', 20, 'Ram', 30]

print("Start code")
try:
    index1 = int(input("Enter value of index1 : "))
    print(list1[index1])
except(ValueError, TypeError, IndexError) as err:
    print(err)
    index1 = int(input("Enter value of index1 : "))
    print(list1[index1])

try:

    index2 = int(input("Enter value of index2 : "))
    print(list1[index2])
except(ValueError, TypeError, IndexError):
    index2 = int(input("Enter value of index2 : "))

try:
    add = list1[index1] + list1[index2]

except(ValueError, TypeError, IndexError):
    print('Handled')




else:
    print(add)

print("End code")


