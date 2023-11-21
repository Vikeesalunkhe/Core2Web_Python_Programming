"""
9. Take Two character from user check if the ascii value both of character are
odd then print the sum of ascii values of character
#Input: char1 = ‘A’
char2 = ‘C’
#Output: 132
#Input: char1 = ‘a’
char2 = ‘b’
#Output:No Output
"""

def addAscii(x,y):
    ascii1 = ord(x)
    ascii2 = ord(y)

    if (ascii1 % 2 == 1) and (ascii2 % 2 == 1):
        return (ascii1 + ascii2)

    else:
        return "not add. is odd"


char1 = input("Enter value of char1 : ")
char2 = input("Enter value of char2 : ")
ret1 = addAscii(char1,char2)
print(ret1)
