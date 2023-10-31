"""
2. WAP to determine whether entered angles define a right-angled triangle.Take three values of angle from the user.

Input1: angel1 = 90
Input2: angle2 = 90
Input3: angle3 = 90
Output:It is a right-angle triangle

Input1: angel1 = 90
Input2: angle2 = 60
Input3: angle3 = 30
Output:It is not a right-angle triangle

"""


angle1 = float(input("Enter value of angle1 : "))
angle2 = float(input("Enter Value of angle2 : "))
angle3 = float(input("Enter value of angle3 : "))

if (angle1 == 90) and (angle1 == 90) and (angle3 == 90):
    print("It is a not right angle triangle")

else:
    print("It is a right angle triangle")
