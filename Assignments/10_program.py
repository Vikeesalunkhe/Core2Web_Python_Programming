"""
10. Program 10: WAP that determines whether a given input year is a leap year or no

"""


year = int(input("Enter value of year : "))


if  (year % 4 == 0) and (year % 100 != 0):

    print("%d is an leap year"%year)

else:

    print("%d is not a leap year"%year)
