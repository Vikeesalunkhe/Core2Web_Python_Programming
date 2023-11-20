"""
6. Program 6: Write a Program to check whether the Character is Alphabet or
not.
Input: v
Output: v is an alphabet.
"""
#A = 65 to Z = 90  a = 97 to z = 122

def Alpha(alpha):

    x = ord(alpha)

    if (x >= 56 and x <= 90) or (x >= 97 and x <= 122 ):
        return ("{} is an alphabet".format(alpha))

    else:
        return ("{} is an not aplphabet".format(alpha))

alphaValue = input("Enter the value og alpha : ")

ret = Alpha(alphaValue)
print(ret)

