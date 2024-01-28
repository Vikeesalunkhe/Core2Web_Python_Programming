#Exception Handling


list1 = [10,'kanha',20,'rahul',30]

try:
    index1 = int(input("Enter value of index1 : "))
    print(list1[index1])

    index2 = int(input("Enter value of index2 : "))
    print(list1[index2])

    add = list1[index1] + list1[index2]

except ValueError:
    print("ValueError Exception Handled")

except TypeError:
    print("TypeErorr Execption Handled")

except IndexError:
    print("IndexError Exception handled")



