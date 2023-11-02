"""
Program 6:
WAP to print all the ASCII values from a given character range.
Input :
Enter the start of range : A
Enter end of range: Z
Output :
ASCII value of A is 65
ASCII value of B is 66
ASCII value of C is 67
.
.
.
ASCII value of Y is 89
"""

start = input("Enter the start value : ")
end = input("Enter the end Value : ")

Ascii1 = ord(start)
Ascii2 = ord(end)

for i in range(Ascii1,Ascii2):
    char = chr(i)
    print("ASCII Value of {} is {} ".format(char,i))
