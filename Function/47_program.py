"""
9. Program 9: Write a program to check whether the input character is a vowel or
consonant
Input: ‘a’
Output: vowel
Input: ‘b’
Output: consonant
"""

#vowel = a(97) ,e(101), i(105),o(111),u(117)

def Vowel(char):

    value = ord(char)
    if (value == 97) or (value == 101) or (value == 105) or (value == 111) or (value == 117):

        print("vowel")

    else:
        print("consonant")

char = input("Enter the char value : ")
Vowel(char)


    
