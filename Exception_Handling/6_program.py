#raise exception

def Voting(name, age):

    if age < 18:
        raise ValueError("not Eligible for Voting")

    else:
        print("thank for Voting")


print("start code")

name = input("Enter name : ")

try:
    age = int(input("Enter value of age : "))

except ValueError:
    print("Enter Proper Int no. :  ")

Voting(name, age)

print("End Code")
