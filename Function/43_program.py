"""
5. Program 5: Write a Program to take an integer ranging from 0 to 6 and print
corresponding weekday (week starting from Monday)
Input: 2
Output: Wednesday.
"""

def WeekDay(day):

    if (day == 0):
        print("Monday")

    elif (day == 1):
        print("Tuesday")

    elif (day == 2):
        print("Wednesday")

    elif (day == 3):
        print("Thursday")

    elif (day == 4):
        print("Friday")

    elif (day == 5):
        print("Saturday")

    else:
        print("Sunday")


dayNo = int(input("Enter the value of Weekday : "))
WeekDay(dayNo)
