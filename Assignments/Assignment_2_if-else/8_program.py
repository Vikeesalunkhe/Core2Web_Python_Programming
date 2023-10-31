"""
8. Take single character from user check if the ascii value of character is Even the print character.
#Input char1 = ‘B’
#Output: B
#Input char1 = ‘C’
#Output: No Output

"""

char1 = input("Enter value of char1 : ")
ascii_value = ord(char1)

if (ascii_value % 2 == 0 ):
    print(char1)

else:
    print("No Output")



