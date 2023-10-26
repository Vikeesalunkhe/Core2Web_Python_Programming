"""
5. Print the "Core2web" string a number of times entered by the user if the number is even.
#Input: num = 2
#Output: Core2web
         Core2web
#Input: num = 5
#Output: No Output

"""

num = int(input("Enter value of num : "))

if (num % 2 == 0):
    for i in range(num):
        print("Core2Web")

else:
    print("No Output")
