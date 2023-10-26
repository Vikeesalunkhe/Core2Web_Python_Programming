"""
9. Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character
#Input: char1 = ‘A’
        char2 = ‘C’
#Output: 132

#Input: char1 = ‘a’
        char2 = ‘b’

"""

char1 = input("Enter value of char1 : ")
char2 = input("Enter value of char2 : ")

ascii_1 = ord(char1)
ascii_2 = ord(char2)

if (ascii_1 % 2 == 1) and (ascii_2 % 2 == 1):
    print(ascii_1 + ascii_2)

else:
    print("No Output")
