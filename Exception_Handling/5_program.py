#Exeption Handling


list1 = [10, 'kanha', 20, 'Ram', 30]

print("Start code")
try:
    index1 = int(input("Enter value of index1 : "))
    print(list1[index1])

    index2 = int(input("Enter value of index2 : "))
    print(list1[index2])

    add = list1[index1] + list1[index2]


except ValueError:
    print("valueError Handeld")

except TypeError:
    print("TypeError Handeld")

except IndexError:
    print("IndexError Handeld")


else:
    print(add)

print("End code")


