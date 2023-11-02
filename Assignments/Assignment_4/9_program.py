"""
Program 9:
WAP to print the count of all negative numbers from a given range
Input:
Start: -15
End: 50
Output:15
"""


start = int(input("Enter the start value : "))
end = int(input("Enter the end value : " ))

count = 0
for i in range(start,end):
    if (i<0):
        count = count + 1



print(count)
