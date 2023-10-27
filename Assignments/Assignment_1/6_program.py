#6. Program 6: Write a Program to check whether the Character is Alphabet or not.
#Input: v
#Output: v is an alphabet.



char = input("Enter your char. : ")

if (len(char) == 1) and (char.isalpha()):
    print("{} is an alphabet".format(char))

else :
    print("{} is an not alphabet".format(char))
