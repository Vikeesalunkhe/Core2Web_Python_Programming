"""
Program 7:
WAP that prints all Positive numbers from a given range.
Input:
Start: -7
End: 8
Output:
1234567
"""


start = int(input("Enter the start value : "))
end = int(input("Enter the end value : "))


for i in range(start,end):

    if (i>=1):
        print(i,end = "")
