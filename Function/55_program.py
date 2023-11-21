"""
8. Take single character from user check if the ascii value of character is
Even the print character.
#Input char1 = ‘B’
#Output: B
#Input char1 = ‘C’
#Output: No Output
"""

def AsciiValue(x):

    no = ord(x)

    if no % 2 == 0:
        return x

    else:
        return "Ascii value is odd"

    

char = input("Enter char value : ")
ret1 = AsciiValue(char)
print(ret1)
