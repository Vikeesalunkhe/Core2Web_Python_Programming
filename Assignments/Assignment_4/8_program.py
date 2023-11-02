"""
Program 8:
WAP to prints numbers which are divisible by 3 and 5 both in a given range.
Input:
Start:15
End: 50
Output:
15 30 45
"""


start = int(input("Enter the start value : "))
end = int(input("Enter the end Value : "))


for i in range(start,end):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i,end = " ")
