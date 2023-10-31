#5. Program 5: Write a Program to take an integer ranging from 0 to 6 and print corresponding weekday (week starting from Monday)
#Input: 2
#Output: Wednesday.


day = int(input("Enter value of day bet(0 to 6) : "))

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
