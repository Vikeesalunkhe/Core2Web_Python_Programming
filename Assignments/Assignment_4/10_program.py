"""
Program 10:
WAP program to calculate and print the product of the count of odd
numbers within a given range.
Input:
Start: 1
End: 11
Output:
3125

"""


start = int(input("Enter the start valuie : "))
end = int(input("Enter the end value : "))

count = 0
for i in range(start,end):
    if (i % 2 == 1):
        count +=1


print(count**count)


