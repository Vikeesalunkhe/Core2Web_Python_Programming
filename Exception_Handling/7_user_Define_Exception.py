class VotingError(Exception):

    def __init__(self, msg):
        super().__init__(msg)


def voting(name, age):

    if age<18:
        raise VotingError("Not Eligible for voting")

    else:
        print("Thanks for Voting")

print("start Code")

name = input("Enter name : ")

try:
    age = int(input("Enter value of age : "))

except ValueError:
    print("add int data ")
    age = int(input("Enter value of age : "))


try:
    voting(name, age)

except VotingError as err:
    print(err)


print("End code")
