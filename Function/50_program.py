"""
2. WAP to determine whether entered angles define a right-angled triangle.
Take three values of angle from the user.
Input1: angel1 = 90
Input2: angle2 = 90
Input3: angle3 = 90
Output:
It is not a right-angle triangle
Input1: angel1 = 90
Input2: angle2 = 60
Input3: angle3 = 30
Output:
It is a right-angle triangle
"""

def CheakTriangle(x,y,z):

    if (x == 90) and (y == 60) and (z == 30):
        print("it is a right-angle triangle")

    else:
        print("it is not a right angle triangle")
    
ang = float(input("Enter value of angle1 : "))
ang2 = float(input("Enter value of angle2 : "))
ang3 = float(input("Enter value of angle3 : "))

ret =  CheakTriangle(ang,ang2,ang3)
